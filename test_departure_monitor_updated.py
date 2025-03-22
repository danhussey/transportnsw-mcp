from api import get_departure_monitor
import pprint
from datetime import datetime, timedelta

def test_stop_id(stop_id, description="", future_time=False):
    """Test a specific stop ID and print the results."""
    print(f"\n{'='*80}")
    print(f"Testing stop ID: {stop_id}" + (f" ({description})" if description else ""))
    print(f"{'='*80}")
    
    # If future_time is True, set the time to 30 minutes from now
    time_param = None
    if future_time:
        future = datetime.now() + timedelta(minutes=30)
        time_param = future.strftime('%H:%M')
        print(f"Using future time: {time_param}")
    
    result = get_departure_monitor(stop_id, time=time_param)
    
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
                    if hasattr(trans, 'disassembled_name'):
                        print(f"  Name: {trans.disassembled_name}")
                    elif hasattr(trans, 'name'):
                        print(f"  Name: {trans.name}")
                    if hasattr(trans, 'destination') and hasattr(trans.destination, 'name'):
                        print(f"  Destination: {trans.destination.name}")
                
                # Display time info
                if hasattr(event, 'departure_time_planned'):
                    print(f"  Planned Departure: {event.departure_time_planned}")
                if hasattr(event, 'departure_time_estimated'):
                    print(f"  Estimated Departure: {event.departure_time_estimated}")
                
                # Display location info
                if hasattr(event, 'location'):
                    loc = event.location
                    if hasattr(loc, 'name'):
                        print(f"  Location: {loc.name}")
                    if hasattr(loc, 'disassembled_name'):
                        print(f"  Platform/Stop: {loc.disassembled_name}")
        else:
            print("\nNo departure events found.")
        
        # Check for locations
        if hasattr(result, 'locations') and result.locations:
            print(f"\nFound {len(result.locations)} locations:")
            for i, location in enumerate(result.locations[:3]):  # Show first 3 locations
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
# Try with the stop IDs from the documentation
test_stop_id("10101331", "Domestic Airport Station (from documentation)")

# Try with the stop IDs we found earlier
test_stop_id("200060", "Central Station global ID")
test_stop_id("200070", "Town Hall Station")
test_stop_id("200080", "Wynyard Station")
test_stop_id("200010", "Circular Quay Station")

# Try with a future time to see if we get more results
test_stop_id("200060", "Central Station with future time", future_time=True)
