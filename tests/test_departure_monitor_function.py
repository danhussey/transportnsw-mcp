from api import get_departure_monitor
import pprint

def run_stop_id_func_test(stop_id, description=""):
    """Test a specific stop ID and print the results."""
    print(f"\n{'='*80}")
    print(f"Testing stop ID: {stop_id}" + (f" ({description})" if description else ""))
    print(f"{'='*80}")
    
    result = get_departure_monitor(stop_id)
    
    if result:
        # Our implementation returns a list of stop events directly
        print(f"\nFound {len(result)} departures:")
        for i, event in enumerate(result[:5]):  # Show first 5 events
            print(f"\nDeparture {i+1}:")
            
            # Display transportation info
            if 'transportation' in event:
                trans = event['transportation']
                if 'number' in trans:
                    print(f"  Line: {trans['number']}")
                if 'disassembledName' in trans:
                    print(f"  Name: {trans['disassembledName']}")
                elif 'name' in trans:
                    print(f"  Name: {trans['name']}")
                if 'destination' in trans and 'name' in trans['destination']:
                    print(f"  Destination: {trans['destination']['name']}")
            
            # Display time info
            if 'departureTimePlanned' in event:
                print(f"  Planned Departure: {event['departureTimePlanned']}")
            if 'departureTimeEstimated' in event:
                print(f"  Estimated Departure: {event['departureTimeEstimated']}")
            
            # Display location info
            if 'location' in event:
                loc = event['location']
                if 'name' in loc:
                    print(f"  Location: {loc['name']}")
                if 'disassembledName' in loc:
                    print(f"  Platform/Stop: {loc['disassembledName']}")
        
        # Print full response for debugging
        print("\nFull response:")
        pp = pprint.PrettyPrinter(indent=2, depth=2)
        pp.pprint(result)
    else:
        print("No result returned from the API.")

# Define pytest test cases
def test_central_station_global_id():
    run_stop_id_func_test("200060", "Central Station global ID")

def test_central_station_stop_id():
    run_stop_id_func_test("10111010", "Central Station stop ID")

def test_user_provided_stop_id():
    run_stop_id_func_test("10111101-0-X1", "User provided stop ID")

def test_town_hall_bus_stop():
    run_stop_id_func_test("209516", "Town Hall Station, Park St, Stand H")

def test_random_stop_id():
    run_stop_id_func_test("2000101", "Random stop ID")

# This allows running the script directly for debugging
if __name__ == "__main__":
    test_central_station_global_id()
    test_central_station_stop_id()
    test_user_provided_stop_id()
    test_town_hall_bus_stop()
    test_random_stop_id()
