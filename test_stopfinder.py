from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from dotenv import load_dotenv
import os
import pprint

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
api_version = '10.2.1.42'  # API version

def find_stop(query):
    """
    Find stops using the stopfinder API.
    
    Args:
        query (str): Search query for stop name
        
    Returns:
        API response containing stop information
    """
    print(f"\n{'='*80}")
    print(f"Searching for stops matching: '{query}'")
    print(f"{'='*80}")
    
    try:
        # Call the stopfinder API
        api_response = api_instance.tfnsw_stopfinder_request(
            output_format=output_format,
            type_sf='stop',  # Search for stops
            name_sf=query,   # Search query
            coord_output_format=coord_output_format,
            version=api_version
        )
        
        if api_response:
            print(f"API Version: {api_response.version}")
            
            # Check for locations
            if hasattr(api_response, 'locations') and api_response.locations:
                print(f"\nFound {len(api_response.locations)} locations:")
                for i, location in enumerate(api_response.locations):
                    print(f"\nLocation {i+1}:")
                    if hasattr(location, 'name'):
                        print(f"  Name: {location.name}")
                    if hasattr(location, 'id'):
                        print(f"  ID: {location.id}")
                    if hasattr(location, 'type'):
                        print(f"  Type: {location.type}")
                    if hasattr(location, 'coord'):
                        print(f"  Coordinates: {location.coord}")
                    
                    # Check for assigned stops
                    if hasattr(location, 'assigned_stops') and location.assigned_stops:
                        print(f"  Assigned Stops: {len(location.assigned_stops)}")
                        for j, stop in enumerate(location.assigned_stops):
                            print(f"    Stop {j+1}:")
                            if hasattr(stop, 'name'):
                                print(f"      Name: {stop.name}")
                            if hasattr(stop, 'id'):
                                print(f"      ID: {stop.id}")
                            if hasattr(stop, 'modes'):
                                print(f"      Modes: {stop.modes}")
            else:
                print("\nNo locations found.")
            
            # Print full response as dictionary for debugging
            print("\nFull response as dictionary:")
            pp = pprint.PrettyPrinter(indent=2)
            pp.pprint(api_response.to_dict())
            
            return api_response
        else:
            print("No response from the API.")
            return None
    except ApiException as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None

def run_departure_monitor_test(stop_id):
    """
    Test the departure monitor API with a specific stop ID.
    
    Args:
        stop_id (str): Stop ID to test
        
    Returns:
        API response containing departure information
    """
    print(f"\n{'='*80}")
    print(f"Testing departure monitor for stop ID: {stop_id}")
    print(f"{'='*80}")
    
    try:
        # Call the departure monitor API
        api_response = api_instance.tfnsw_dm_request(
            output_format=output_format,
            coord_output_format=coord_output_format,
            type_dm='stop',  # Type is 'stop' for stop IDs
            name_dm=stop_id,
            version=api_version
        )
        
        if api_response:
            print(f"API Version: {api_response.version}")
            
            # Check for stop events
            if hasattr(api_response, 'stop_events') and api_response.stop_events:
                print(f"\nFound {len(api_response.stop_events)} departures:")
                for i, event in enumerate(api_response.stop_events):
                    print(f"\nDeparture {i+1}:")
                    
                    # Display transportation info
                    if hasattr(event, 'transportation'):
                        trans = event.transportation
                        if hasattr(trans, 'number'):
                            print(f"  Line: {trans.number}")
                        if hasattr(trans, 'name'):
                            print(f"  Name: {trans.name}")
                        if hasattr(trans, 'destination') and hasattr(trans.destination, 'name'):
                            print(f"  Destination: {trans.destination.name}")
                    
                    # Display time info
                    if hasattr(event, 'departure_time_planned'):
                        print(f"  Planned Departure: {event.departure_time_planned}")
                    if hasattr(event, 'departure_time_estimated'):
                        print(f"  Estimated Departure: {event.departure_time_estimated}")
            else:
                print("\nNo departure events found.")
            
            # Check for locations
            if hasattr(api_response, 'locations') and api_response.locations:
                print(f"\nFound {len(api_response.locations)} locations:")
                for i, location in enumerate(api_response.locations):
                    print(f"\nLocation {i+1}:")
                    if hasattr(location, 'name'):
                        print(f"  Name: {location.name}")
                    if hasattr(location, 'id'):
                        print(f"  ID: {location.id}")
                    if hasattr(location, 'type'):
                        print(f"  Type: {location.type}")
            
            # Print full response as dictionary for debugging
            print("\nFull response as dictionary:")
            pp = pprint.PrettyPrinter(indent=2)
            pp.pprint(api_response.to_dict())
            
            return api_response
        else:
            print("No response from the API.")
            return None
    except ApiException as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None

# Define test functions for pytest
def test_find_central_station():
    response = find_stop("Central Station")
    assert response is not None
    assert hasattr(response, 'locations')
    assert len(response.locations) > 0
    return response

def test_find_town_hall_station():
    response = find_stop("Town Hall Station")
    assert response is not None
    assert hasattr(response, 'locations')
    assert len(response.locations) > 0
    return response

def test_find_wynyard_station():
    response = find_stop("Wynyard Station")
    assert response is not None
    assert hasattr(response, 'locations')
    assert len(response.locations) > 0
    return response

def test_find_circular_quay():
    response = find_stop("Circular Quay")
    assert response is not None
    assert hasattr(response, 'locations')
    assert len(response.locations) > 0
    return response

def test_departure_monitor_central():
    # Use a hardcoded stop ID for Central Station
    run_departure_monitor_test("200060")

def test_departure_monitor_town_hall():
    # Use a hardcoded stop ID for Town Hall Station
    run_departure_monitor_test("200070")

# This allows running the script directly for debugging
if __name__ == "__main__":
    # Find stops first
    central_response = test_find_central_station()
    town_hall_response = test_find_town_hall_station()
    wynyard_response = test_find_wynyard_station()
    circular_quay_response = test_find_circular_quay()
    
    # Extract stop IDs from the responses
    stop_ids = []
    for response in [central_response, town_hall_response, wynyard_response, circular_quay_response]:
        if response and hasattr(response, 'locations'):
            for location in response.locations:
                if hasattr(location, 'id'):
                    stop_ids.append(location.id)
                    
                # Also check assigned stops
                if hasattr(location, 'assigned_stops'):
                    for stop in location.assigned_stops:
                        if hasattr(stop, 'id'):
                            stop_ids.append(stop.id)
    
    # Test departure monitor with the found stop IDs
    print("\n\nTesting departure monitor with found stop IDs:")
    for stop_id in stop_ids[:5]:  # Test first 5 stop IDs
        run_departure_monitor_test(stop_id)
        
    # Also run the fixed test cases
    test_departure_monitor_central()
    test_departure_monitor_town_hall()
