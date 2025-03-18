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


def test_coordinate_api():
    """
    Test function to verify coordinate API responses and diagnose issues.
    This helps understand why certain parameters may not work as expected.
    """
    import time
    
    print("\n=== Transport NSW Coordinate API Test ===\n")
    
    # Test 1: Bus stops (known to work)
    print("Test 1: Find bus stops around Central Station")
    try:
        start_time = time.time()
        bus_stops = find_transport_stops(coord, stop_type='BUS_POINT', radius=500)
        elapsed = time.time() - start_time
        print(f"  Status: {'✓ Success' if bus_stops else '✗ Failed'}")
        print(f"  Response time: {elapsed:.2f} seconds")
        print(f"  Found locations: {len(bus_stops.locations) if hasattr(bus_stops, 'locations') else 0}")
        if hasattr(bus_stops, 'locations') and bus_stops.locations:
            # Check the type values in the response
            types = set(getattr(loc, 'type', 'unknown') for loc in bus_stops.locations[:10])
            print(f"  Location types in response: {types}")
    except Exception as e:
        print(f"  Error: {str(e)}")
    
    # Test 2: POI points (known to work)
    print("\nTest 2: Find POIs around Central Station")
    try:
        start_time = time.time()
        poi_locations = find_transport_stops(coord, stop_type='POI_POINT', radius=500)
        elapsed = time.time() - start_time
        print(f"  Status: {'✓ Success' if poi_locations else '✗ Failed'}")
        print(f"  Response time: {elapsed:.2f} seconds")
        print(f"  Found locations: {len(poi_locations.locations) if hasattr(poi_locations, 'locations') else 0}")
        if hasattr(poi_locations, 'locations') and poi_locations.locations:
            # Check the type values in the response
            types = set(getattr(loc, 'type', 'unknown') for loc in poi_locations.locations[:10])
            print(f"  Location types in response: {types}")
    except Exception as e:
        print(f"  Error: {str(e)}")
    
    # Test 3: GIS_POINT (known to fail)
    print("\nTest 3: GIS_POINT test (expected to fail)")
    try:
        start_time = time.time()
        gis_locations = api_instance.tfnsw_coord_request(
            output_format=output_format,
            coord=coord,
            coord_output_format=coord_output_format,
            incl_filter=incl_filter,
            type_1='GIS_POINT',
            radius_1=500,
            version='10.2.1.42'
        )
        elapsed = time.time() - start_time
        print(f"  Status: Unexpected success")
        print(f"  Response time: {elapsed:.2f} seconds")
    except Exception as e:
        print(f"  Status: ✓ Expected error")
        print(f"  Error type: {type(e).__name__}")
        print(f"  Error message: {str(e)}")
        print("\n  Explanation: The GIS_POINT parameter causes the API to return locations with type='gis',")
        print("  but the API client expects types to be one of: ['poi', 'singlehouse', 'stop', 'platform',")
        print("  'street', 'locality', 'suburb', 'gisPoint', 'unknown']. This causes a validation error.")
    
    print("\n=== Test Complete ===\n")


# Run the test if called with --test argument
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_coordinate_api()