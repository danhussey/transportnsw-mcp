import sys
import os

# Add the parent directory to path so we can import the api module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import get_departure_monitor
import json
import pprint

# Test with the provided stop ID
stop_id = "10111101-0-X1"
result = get_departure_monitor(stop_id)

# Print the result in a readable format
if result:
    print(f"\nFound {len(result)} departures:")
    
    # Display the first few departures with details
    for i, departure in enumerate(result[:5]):  # Show first 5 departures
        print(f"\nDeparture {i+1}:")
        
        # Print key departure information
        if 'stop_name' in departure:
            print(f"  Stop: {departure['stop_name']}")
        if 'route_number' in departure:
            print(f"  Route: {departure['route_number']}")
        if 'route_name' in departure:
            print(f"  Name: {departure['route_name']}")
        if 'destination' in departure:
            print(f"  Destination: {departure['destination']}")
        if 'operator' in departure:
            print(f"  Operator: {departure['operator']}")
        if 'local_departure_time' in departure:
            print(f"  Local Departure Time: {departure['local_departure_time']}")
        if 'planned_departure' in departure:
            print(f"  Planned Departure: {departure['planned_departure']}")
        if 'estimated_departure' in departure:
            print(f"  Estimated Departure: {departure['estimated_departure']}")
        if 'wheelchair_access' in departure:
            print(f"  Wheelchair Access: {departure['wheelchair_access']}")
    
    # Print full response for debugging
    print("\nFull response:")
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(result)
else:
    print("No result returned from the API.")
