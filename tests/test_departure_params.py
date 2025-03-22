from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from dotenv import load_dotenv
import os
from datetime import datetime
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

# Import our direct implementation
from api import get_departure_monitor

def run_departure_params_test(stop_id, description=""):
    """Test departure monitor with different parameter combinations."""
    print(f"\n{'='*80}")
    print(f"Testing departure monitor for stop ID: {stop_id}" + (f" ({description})" if description else ""))
    print(f"{'='*80}")
    
    # Try with different parameters
    try:
        # Try with date and time parameters
        now = datetime.now()
        date_str = now.strftime('%d-%m-%Y')  # Format: DD-MM-YYYY for our function
        time_str = now.strftime('%H:%M')    # Format: HH:MM for our function
        
        print(f"Trying with date={date_str} and time={time_str}")
        result = get_departure_monitor(stop_id, date=date_str, time=time_str)
        
        if result and len(result) > 0:
            print(f"Success! Found {len(result)} departures.")
            
            # Print first few results
            for i, event in enumerate(result[:3]):
                print(f"\nDeparture {i+1}:")
                if 'transportation' in event and 'number' in event['transportation']:
                    print(f"  Line: {event['transportation']['number']}")
                if 'transportation' in event and 'destination' in event['transportation']:
                    print(f"  Destination: {event['transportation']['destination']['name']}")
                if 'departureTimePlanned' in event:
                    print(f"  Planned: {event['departureTimePlanned']}")
            
            return result
        else:
            print("No departure events found with date and time parameters.")
        
        # Try with mot_type parameter (1 = Train)
        print("\nTrying with mot_type=1 (Train)")
        result = get_departure_monitor(stop_id, mot_type=1)
        
        if result and len(result) > 0:
            print(f"Success! Found {len(result)} train departures.")
            return result
        else:
            print("No train departures found.")
        
        # Try with mot_type parameter (5 = Bus)
        print("\nTrying with mot_type=5 (Bus)")
        result = get_departure_monitor(stop_id, mot_type=5)
        
        if result and len(result) > 0:
            print(f"Success! Found {len(result)} bus departures.")
            return result
        else:
            print("No bus departures found.")
        
        # Try with max_results parameter
        print("\nTrying with max_results=10")
        result = get_departure_monitor(stop_id, max_results=10)
        
        if result and len(result) > 0:
            print(f"Success! Found {len(result)} departures with max_results=10.")
            return result
        else:
            print("No departures found with max_results=10.")
        
        # If all attempts fail, return None
        return None
    except Exception as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None

# Define pytest test cases
def test_central_station_params():
    run_departure_params_test("200060", "Central Station")

def test_town_hall_station_params():
    run_departure_params_test("200070", "Town Hall Station")

def test_wynyard_station_params():
    run_departure_params_test("200080", "Wynyard Station")

def test_circular_quay_station_params():
    run_departure_params_test("200010", "Circular Quay Station")

# This allows running the script directly for debugging
if __name__ == "__main__":
    test_central_station_params()
    test_town_hall_station_params()
    test_wynyard_station_params()
    test_circular_quay_station_params()
