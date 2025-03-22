from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()
API_KEY = os.getenv('OPEN_TRANSPORT_API_KEY')

# Configure API key authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = API_KEY
configuration.api_key_prefix['Authorization'] = 'apikey'

# Create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

# Define common parameters for API requests
output_format = 'rapidJSON'  # Required for JSON output
coord_output_format = 'EPSG:4326'  # Standard coordinate format
incl_filter = 1  # Enable advanced filter mode
api_version = '10.2.1.42'  # API version

# Import MCP server
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Transport NSW")

@mcp.tool()
def find_transport_stops(location_coord, stop_type='BUS_POINT', radius=100):
    """
    Find transport stops around a specific location.
    
    Args:
        location_coord (str): Coordinates in format 'LONGITUDE:LATITUDE:EPSG:4326'
        stop_type (str): Type of stops to find: 'BUS_POINT', 'POI_POINT', or 'GIS_POINT'
        radius (int): Search radius in meters
        
    Returns:
        API response with transport stops
    """
    try:
        api_response = api_instance.tfnsw_coord_request(
            output_format=output_format,
            coord=location_coord,
            coord_output_format=coord_output_format,
            incl_filter=incl_filter,
            type_1=stop_type,
            radius_1=radius,
            version=api_version
        )
        return api_response
    except ApiException as e:
        print(f"Exception when calling DefaultApi->tfnsw_coord_request: {e}\n")
        return None

@mcp.tool()
def get_transport_alerts(date=None, mot_type=None, stop_id=None, line_number=None, operator_id=None):
    """
    Get transport alerts from the Transport NSW API.
    
    Args:
        date (str, optional): Date in DD-MM-YYYY format. Defaults to today's date.
        mot_type (int, optional): Mode of transport type filter. Options:
            1: Train
            2: Metro
            4: Light Rail
            5: Bus
            7: Coach
            9: Ferry
            11: School Bus
        stop_id (str, optional): Stop ID or global stop ID to filter by.
        line_number (str, optional): Line number to filter by (e.g., '020T1').
        operator_id (str, optional): Operator ID to filter by.
    
    Returns:
        dict: API response containing alerts information
    """
    # Set default date to today if not provided
    if date is None:
        date = datetime.now().strftime('%d-%m-%Y')
    
    # Required parameter
    kwargs = {
        'filter_date_valid': date,
        'version': api_version
    }
    
    # Add optional filters if provided
    if mot_type is not None:
        kwargs['filter_mot_type'] = mot_type
    
    if stop_id is not None:
        kwargs['itd_l_pxx_sel_stop'] = stop_id
    
    if line_number is not None:
        kwargs['itd_l_pxx_sel_line'] = line_number
    
    if operator_id is not None:
        kwargs['itd_l_pxx_sel_operator'] = operator_id
    
    try:
        # Call the API
        api_response = api_instance.tfnsw_addinfo_request(output_format, **kwargs)
        return api_response
    except ApiException as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None

# # Call the API to get next departing i.e. timetable information for a specific stop
# @mcp.tool()
# def get_next_departure(stop_id, direction=None, date=None, mot_type=None, operator_id=None):
#     """
#     Get next departing i.e. timetable information for a specific stop from the Trip Planner API.
    
#     Args:
#         stop_id (str): Stop ID or global stop ID
#         direction (str, optional): Direction of travel (e.g., 'N' for north, 'S' for south)
#         date (str, optional): Date in DD-MM-YYYY format. Defaults to today's date.
#         mot_type (int, optional): Mode of transport type filter. Options:
#             1: Train
#             2: Metro
#             4: Light Rail
#             5: Bus
#             7: Coach
#             9: Ferry
#             11: School Bus
#         operator_id (str, optional): Operator ID to filter by.
        
#     Returns:
#         dict: API response containing timetable information
#     """
#     # Set default date to today if not provided
#     if date is None:
#         date = datetime.now().strftime('%d-%m-%Y')
    
#     # Required parameters
#     kwargs = {
#         'itd_l_pxx_sel_stop': stop_id,
#         'filter_date_valid': date,
#         'version': api_version
#     }
    
#     # Add optional filters if provided
#     # Direction is not directly supported by the API, so we'll skip it for now
#     # if direction is not None:
#     #     kwargs['filter_direction'] = direction
    
#     if mot_type is not None:
#         kwargs['filter_mot_type'] = mot_type
    
#     if operator_id is not None:
#         kwargs['itd_l_pxx_sel_operator'] = operator_id
    
#     try:
#         # Call the API
#         api_response = api_instance.tfnsw_addinfo_request(output_format, **kwargs)
#         return api_response
#     except ApiException as e:
#         print(f"Exception when calling Transport NSW API: {e}\n")
#         return None


# Call the API to get real-time departure information for a specific stop
@mcp.tool()
def get_departure_monitor(stop_id, date=None, time=None, mot_type=None, max_results=3):
    """
    Get real-time departure monitor information for a specific stop from the Trip Planner API.
    This function uses direct HTTP requests to the Transport NSW API.
    
    Args:
        stop_id (str): Stop ID or global stop ID
        date (str, optional): Date in DD-MM-YYYY format. Defaults to today's date.
        time (str, optional): Time in HH:MM format. Defaults to current time.
        mot_type (int, optional): Mode of transport type filter. Options:
            1: Train
            2: Metro
            4: Light Rail
            5: Bus
            7: Coach
            9: Ferry
            11: School Bus
        max_results (int, optional): Maximum number of results to return. Default is 3.
        
    Returns:
        dict: API response containing departure information
    """
    import requests
    
    # API endpoint
    API_ENDPOINT = 'https://api.transport.nsw.gov.au/v1/tp/departure_mon'
    
    # Set default date and time to now if not provided
    now = datetime.now()
    
    # Format date as YYYYMMDD for the API
    if date is None:
        itd_date = now.strftime('%Y%m%d')
    else:
        # Convert from DD-MM-YYYY to YYYYMMDD
        day, month, year = date.split('-')
        itd_date = f"{year}{month}{day}"
    
    # Format time as HHMM for the API
    if time is None:
        itd_time = now.strftime('%H%M')
    else:
        # Convert from HH:MM to HHMM
        itd_time = time.replace(':', '')
    
    # Set up the request parameters exactly as in the documentation
    params = {
        'outputFormat': 'rapidJSON',
        'coordOutputFormat': 'EPSG:4326',
        'mode': 'direct',
        'type_dm': 'stop',
        'name_dm': stop_id,
        'depArrMacro': 'dep',
        'itdDate': itd_date,
        'itdTime': itd_time,
        'TfNSWDM': 'true',
        'version': api_version,
        'radius_dm': 100
    }
    
    # Add mot_type filter if provided
    if mot_type is not None:
        params['motType'] = mot_type
    
    # Set up the headers with the API key
    headers = {
        'Authorization': f'apikey {API_KEY}'
    }
    
    try:
        # Make the request
        response = requests.get(API_ENDPOINT, params=params, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Limit the number of stop events to max_results if specified
            if 'stopEvents' in data and len(data['stopEvents']) > max_results:
                data['stopEvents'] = data['stopEvents'][:max_results]
                print(f"Limited results to {max_results} departures")
            
            # Process response
            stops = data.get('stopEvents', [])
            # Sort stops by distance
            stops.sort(key=lambda x: x.get('distance', float('inf')))
            return stops
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response text: {response.text[:500]}...")  # Print first 500 chars
            return None
    except Exception as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None
