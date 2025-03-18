from __future__ import print_function
import time
from pprint import pprint
import os
from api import find_transport_stops, API_KEY, api_version

# Central Station coordinates
CENTRAL_STATION_COORD = '151.206290:-33.884080:EPSG:4326'

def display_location_info(locations, location_type="Stop"):
    """Helper function to display location information"""
    if locations and hasattr(locations, 'locations') and locations.locations:
        print(f"Found {len(locations.locations)} {location_type.lower()}s")
        for i, location in enumerate(locations.locations[:5], 1):  # Show first 5 locations
            print(f"\n{location_type} {i}: {getattr(location, 'name', 'N/A')}")
            print(f"  ID: {getattr(location, 'id', 'N/A')}")
            print(f"  Type: {getattr(location, 'type', 'N/A')}")
            if hasattr(location, 'coord') and location.coord:
                print(f"  Coordinates: {location.coord}")
        return True
    else:
        print(f"No {location_type.lower()}s found or error occurred")
        return False

def demo_coordinate_api():
    """Demonstrate the Transport NSW Coordinate API"""
    print("\n=== Transport NSW Coordinate API Demo ===\n")
    
    # CURL Request Example
    print("CURL Request Example:")
    print(f'''
    curl -X GET "https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord={CENTRAL_STATION_COORD}&coordOutputFormat=EPSG:4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&version={api_version}" \
      -H "Authorization: apikey YOUR_API_KEY" \
      -H "Accept: application/json"
    
    This request will find all bus stops within 1000 meters of Central Station in Sydney.
    ''')
    
    # Example 1: Find bus stops around Central Station
    print("\n1. Finding bus stops around Central Station:")
    bus_stops = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=500)
    display_location_info(bus_stops, "Stop")
    
    # Example 2: Find POI around Central Station
    print("\n2. Finding POIs around Central Station:")
    poi_locations = find_transport_stops(CENTRAL_STATION_COORD, stop_type='POI_POINT', radius=500)
    display_location_info(poi_locations, "POI")
    
    # Example 3: Generate a curl command with your API key
    print("\n3. Curl command for your API key:")
    curl_command = f'''
    curl -X GET "https://api.transport.nsw.gov.au/v1/tp/coord?outputFormat=rapidJSON&coord={CENTRAL_STATION_COORD}&coordOutputFormat=EPSG:4326&inclFilter=1&type_1=BUS_POINT&radius_1=1000&version={api_version}" \
      -H "Authorization: apikey {API_KEY}" \
      -H "Accept: application/json"
    '''
    print(curl_command)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        from test_api import TestCoordinateAPI
        import pytest
        pytest.main(["-v", "test_api.py"])
    else:
        demo_coordinate_api()