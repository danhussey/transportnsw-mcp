from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from dotenv import load_dotenv
import os

load_dotenv()
# get api key from env
API_KEY = os.getenv('OPEN_TRANSPORT_API_KEY')

# Configure API key authorization: APIKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = API_KEY
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['Authorization'] = 'apikey'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

# Define parameters for the API request
output_format = 'rapidJSON'  # Required for JSON output
coord_output_format = 'EPSG:4326'  # Standard coordinate format
incl_filter = 1  # Enable advanced filter mode

# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Transport NSW")

# Add an addition tool
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
            version='10.2.1.42'
        )
        return api_response
    except ApiException as e:
        print(f"Exception when calling DefaultApi->tfnsw_coord_request: {e}\n")
        return None



