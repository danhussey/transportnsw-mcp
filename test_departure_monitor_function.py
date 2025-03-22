from api import get_departure_monitor
import pprint

def test_stop_id(stop_id, description=""):
    """Test a specific stop ID and print the results."""
    print(f"\n{'='*80}")
    print(f"Testing stop ID: {stop_id}" + (f" ({description})" if description else ""))
    print(f"{'='*80}")
    
    result = get_departure_monitor(stop_id)
    
    if result:
        print(f"API Version: {result.version}")
        
        # Check for stop events
        if hasattr(result, 'stop_events') and result.stop_events:
            print(f"\nFound {len(result.stop_events)} departures:")
            for i, event in enumerate(result.stop_events[:5]):  # Show first 5 events
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
        if hasattr(result, 'locations') and result.locations:
            print(f"\nFound {len(result.locations)} locations:")
            for i, location in enumerate(result.locations[:5]):  # Show first 5 locations
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
        pp.pprint(result.to_dict())
    else:
        print("No result returned from the API.")

# Test with various stop IDs
# Central Station
test_stop_id("200060", "Central Station global ID")

# Try a different format of stop ID
test_stop_id("10111010", "Central Station stop ID")

# Try the original stop ID from the user
test_stop_id("10111101-0-X1", "User provided stop ID")

# Try a bus stop ID
test_stop_id("209516", "Town Hall Station, Park St, Stand H")

# Try a different format
test_stop_id("2000101", "Random stop ID")
