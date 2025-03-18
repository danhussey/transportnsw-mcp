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
def find_transport_stops(location_coord, stop_type='BUS_POINT', radius=1000):
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
