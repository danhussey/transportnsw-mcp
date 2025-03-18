from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
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

# CURL Request Example
'''
To execute this curl request, replace YOUR_API_KEY with your actual API key:

curl -X GET "https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord=151.206290:-33.884080:EPSG:4326&coordOutputFormat=EPSG:4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&version=10.2.1.42" \
  -H "Authorization: apikey YOUR_API_KEY" \
  -H "Accept: application/json"

This request will find all bus stops within 1000 meters of Central Station in Sydney.
'''

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

# Define parameters for the API request
output_format = 'rapidJSON'  # Required for JSON output
coord = '151.206290:-33.884080:EPSG:4326'  # Central Station coordinates
coord_output_format = 'EPSG:4326'  # Standard coordinate format
incl_filter = 1  # Enable advanced filter mode


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


# Example 1: Find bus stops around Central Station
print("\n1. Finding bus stops around Central Station:")
bus_stops = find_transport_stops(coord, stop_type='BUS_POINT', radius=500)
if bus_stops and hasattr(bus_stops, 'locations') and bus_stops.locations:
    print(f"Found {len(bus_stops.locations)} bus stops near Central Station")
    for i, location in enumerate(bus_stops.locations[:5], 1):  # Show first 5 stops
        print(f"\nStop {i}: {getattr(location, 'name', 'N/A')}")
        print(f"  ID: {getattr(location, 'id', 'N/A')}")
        print(f"  Type: {getattr(location, 'type', 'N/A')}")
        if hasattr(location, 'coord') and location.coord:
            print(f"  Coordinates: {location.coord}")

# Example 2: Find POI around Central Station
print("\n2. Finding POIs around Central Station:")
poi_locations = find_transport_stops(coord, stop_type='POI_POINT', radius=500)
if poi_locations and hasattr(poi_locations, 'locations') and poi_locations.locations:
    print(f"Found {len(poi_locations.locations)} points of interest near Central Station")
    for i, location in enumerate(poi_locations.locations[:5], 1):  # Show first 5 POIs
        print(f"\nPOI {i}: {getattr(location, 'name', 'N/A')}")
        print(f"  ID: {getattr(location, 'id', 'N/A')}")
        print(f"  Type: {getattr(location, 'type', 'N/A')}")
        if hasattr(location, 'coord') and location.coord:
            print(f"  Coordinates: {location.coord}")
else:
    print("No POIs found or error occurred")

# Example 3: Generate a curl command with your API key
print("\n3. Curl command for your API key:")
curl_command = f'''
curl -X GET "https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord=151.206290:-33.884080:EPSG:4326&coordOutputFormat=EPSG:4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&version=10.2.1.42" \
  -H "Authorization: apikey {API_KEY}" \
  -H "Accept: application/json"
'''
print(curl_command)