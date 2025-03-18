from __future__ import print_function
import time
from pprint import pprint
import os
from api import find_transport_stops, API_KEY

# CURL Request Example
'''
To execute this curl request, replace YOUR_API_KEY with your actual API key:

curl -X GET "https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord=151.206290:-33.884080:EPSG:4326&coordOutputFormat=EPSG:4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&version=10.2.1.42" \
  -H "Authorization: apikey YOUR_API_KEY" \
  -H "Accept: application/json"

This request will find all bus stops within 1000 meters of Central Station in Sydney.
'''

# Central Station coordinates
coord = '151.206290:-33.884080:EPSG:4326'


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


# Import test_coordinate_api has been moved to test_api.py


# Run the test if called with --test argument
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_coordinate_api()