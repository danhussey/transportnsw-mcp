from api import get_departure_monitor
import pprint
from datetime import datetime, timedelta

def _test_stop_id(stop_id, description="", future_time=False, mot_type=None):
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
    
    # Call the API function
    result = get_departure_monitor(stop_id, time=time_param, mot_type=mot_type)
    
    if result:
        # Check for stop events
        if 'stopEvents' in result and result['stopEvents']:
            print(f"\nFound {len(result['stopEvents'])} departures:")
            for i, event in enumerate(result['stopEvents'][:5]):  # Show first 5 events
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
        else:
            print("\nNo departure events found.")
        
        # Check for locations
        if 'locations' in result and result['locations']:
            print(f"\nFound {len(result['locations'])} locations:")
            for i, location in enumerate(result['locations'][:3]):  # Show first 3 locations
                print(f"\nLocation {i+1}:")
                if 'name' in location:
                    print(f"  Name: {location['name']}")
                if 'id' in location:
                    print(f"  ID: {location['id']}")
                if 'type' in location:
                    print(f"  Type: {location['type']}")
                
                # Check for assigned stops
                if 'assignedStops' in location and location['assignedStops']:
                    print(f"  Assigned Stops: {len(location['assignedStops'])}")
                    for j, stop in enumerate(location['assignedStops']):
                        print(f"    Stop {j+1}:")
                        if 'name' in stop:
                            print(f"      Name: {stop['name']}")
                        if 'id' in stop:
                            print(f"      ID: {stop['id']}")
                        if 'productClasses' in stop:
                            print(f"      Product Classes: {stop['productClasses']}")
        
        # Print full response as dictionary for debugging (truncated for readability)
        print("\nResponse summary:")
        pp = pprint.PrettyPrinter(indent=2, depth=2)
        pp.pprint(result)
    else:
        print("No result returned from the API.")

def _verify_departures(response):
    if 'stopEvents' in response and response['stopEvents']:
        print(f"\nFound {len(response['stopEvents'])} departures:")
        for i, event in enumerate(response['stopEvents'][:5]):  # Show first 5 events
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
    else:
        print("\nNo departure events found.")

import pytest

# Parameterized tests
@pytest.mark.parametrize('stop_id', [
    '209937',  # Central Station
    '209939',  # Town Hall Station
    '209940',  # Wynyard Station
])
def test_basic_stop_ids(stop_id):
    result = get_departure_monitor(stop_id)
    assert result is not None
    _verify_departures(result)

@pytest.mark.parametrize('stop_id, mot_type', [
    ('200060', 1),  # Trains only
    ('200070', 4),  # Buses only
    ('200080', 5),  # Ferries only
])
def test_transport_modes(stop_id, mot_type):
    result = get_departure_monitor(stop_id, mot_type=mot_type)
    assert result is not None
    _verify_departures(result)

@pytest.mark.parametrize('stop_id, description, future_time, mot_type', [
    ('10101331', "Domestic Airport Station (from documentation)", False, None),
    ('200060', "Central Station (Trains only)", False, 1),
    ('200070', "Town Hall Station", False, None),
    ('200080', "Wynyard Station", False, None),
    ('200010', "Circular Quay Station", False, None),
    ('200060', "Central Station with future time", True, None),
])
def test_stop_ids_with_params(stop_id, description, future_time, mot_type):
    _test_stop_id(stop_id, description, future_time, mot_type)
