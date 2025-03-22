#!/usr/bin/env python3
"""
Transport NSW API Demo Script

This script demonstrates the main functionality of the Transport NSW API wrapper.
It includes examples of:
- Finding transport stops by name or coordinates
- Getting transport alerts
- Monitoring real-time departures

Requirements:
- Environment variable OPEN_TRANSPORT_API_KEY must be set
"""

import os
import pprint
from datetime import datetime, timedelta
import argparse
from api import (
    find_transport_stops,
    get_transport_alerts,
    get_departure_monitor
)

pp = pprint.PrettyPrinter(indent=2)


def find_stops_demo():
    """Demonstrate finding transport stops by name and coordinates."""
    print("\n" + "="*80)
    print(" FINDING TRANSPORT STOPS ".center(80, "="))
    print("="*80)
    
    # Example 1: Find stops by name
    stop_name = "Central Station"
    print(f"\n1. Finding stops matching: '{stop_name}'")
    
    stops = find_transport_stops(stop_name=stop_name)
    if stops:
        print(f"  Found {len(stops['locations'])} locations")
        
        # Display the first result in detail
        if stops['locations']:
            location = stops['locations'][0]
            print("\n  First result:")
            print(f"    Name: {location.get('name', 'N/A')}")
            print(f"    ID: {location.get('id', 'N/A')}")
            print(f"    Type: {location.get('type', 'N/A')}")
            
            if 'coord' in location:
                lat, lon = location['coord']
                print(f"    Coordinates: {lat}, {lon}")
            
            # Show assigned stops if available
            if 'assigned_stops' in location and location['assigned_stops']:
                print(f"\n    Assigned Stops ({len(location['assigned_stops'])}):")
                for i, stop in enumerate(location['assigned_stops'][:3], 1):  # Show first 3
                    print(f"      Stop {i}:")
                    print(f"        Name: {stop.get('name', 'N/A')}")
                    print(f"        ID: {stop.get('id', 'N/A')}")
                    print(f"        Modes: {stop.get('modes', 'N/A')}")
    
    # Example 2: Find stops by coordinates
    print("\n2. Finding stops near coordinates (Central Station area)")
    coords = "151.206290:-33.884080:EPSG:4326"  # Central Station coordinates
    radius = 500  # meters
    
    nearby_stops = find_transport_stops(coord=coords, radius=radius)
    if nearby_stops:
        print(f"  Found {len(nearby_stops['locations'])} locations within {radius}m")
        
        # Count transport modes
        modes_count = {}
        for location in nearby_stops['locations']:
            if 'assigned_stops' in location:
                for stop in location['assigned_stops']:
                    if 'modes' in stop:
                        for mode in stop['modes']:
                            modes_count[mode] = modes_count.get(mode, 0) + 1
        
        # Display transport mode counts
        if modes_count:
            print("\n  Transport modes available:")
            mode_names = {
                1: "Train", 2: "Metro", 4: "Light Rail", 
                5: "Bus", 7: "Coach", 9: "Ferry", 11: "School Bus"
            }
            for mode_id, count in sorted(modes_count.items()):
                mode_name = mode_names.get(mode_id, f"Mode {mode_id}")
                print(f"    {mode_name}: {count} stops")
    
    print("\nSee full response structure for more details:")
    print("pp.pprint(stops)  # Uncomment to see full structure")


def get_alerts_demo():
    """Demonstrate getting transport alerts."""
    print("\n" + "="*80)
    print(" TRANSPORT ALERTS ".center(80, "="))
    print("="*80)
    
    # Example 1: Get all alerts
    print("\n1. Getting all current transport alerts")
    
    alerts = get_transport_alerts()
    if alerts:
        # Display summary
        print(f"  Retrieved alerts successfully!")
        print(f"  Found {len(alerts)} alerts")
        
        # Categorize alerts by type
        alert_types = {}
        for alert in alerts:
            alert_type = alert.get('priority', 'Unknown')
            alert_types[alert_type] = alert_types.get(alert_type, 0) + 1
        
        # Display alert type counts
        if alert_types:
            print("\n  Alert priorities:")
            for priority, count in sorted(alert_types.items()):
                print(f"    {priority}: {count} alerts")
        
        # Show a few examples
        if len(alerts) > 0:
            print("\n  Example alerts:")
            for i, alert in enumerate(alerts[:3], 1):  # Show first 3
                print(f"\n    Alert {i}:")
                print(f"      Title: {alert.get('title', 'N/A')}")
                print(f"      Priority: {alert.get('priority', 'N/A')}")
                if 'description' in alert:
                    desc = alert.get('description', '')
                    # Truncate long descriptions
                    if len(desc) > 100:
                        desc = desc[:97] + "..."
                    print(f"      Description: {desc}")
    
    # Example 2: Get train alerts only
    print("\n2. Getting train alerts only")
    train_alerts = get_transport_alerts(mot_type=1)  # 1 = Train
    
    if train_alerts:
        print(f"  Found {len(train_alerts)} train alerts")
    else:
        print("  No train alerts found or error occurred")


def monitor_departures_demo():
    """Demonstrate monitoring real-time departures."""
    print("\n" + "="*80)
    print(" REAL-TIME DEPARTURES ".center(80, "="))
    print("="*80)
    
    # Example 1: Get departures for Central Station
    stop_id = "200060"  # Central Station
    print(f"\n1. Getting departures from Central Station (ID: {stop_id})")
    
    departures = get_departure_monitor(stop_id, max_results=5)
    if departures:
        print(f"  Found {len(departures)} departures")
        
        # Show detailed information for the first few departures
        print("\n  Next departures:")
        for i, departure in enumerate(departures[:5], 1):
            print(f"\n    Departure {i}:")
            print(f"      Route: {departure.get('route_number', 'N/A')}")
            print(f"      Direction: {departure.get('destination', 'N/A')}")
            
            # Show times
            local_time = departure.get('local_departure_time', 'N/A')
            planned = departure.get('planned_departure', 'N/A')
            estimated = departure.get('estimated_departure', 'N/A')
            
            print(f"      Local Time: {local_time}")
            print(f"      Planned: {planned}")
            print(f"      Estimated: {estimated}")
            
            # Calculate delay if available
            if planned != 'N/A' and estimated != 'N/A':
                if planned != estimated:
                    print(f"      Status: DELAYED")
                else:
                    print(f"      Status: On time")
    
    # Example 2: Get departures for a specific time
    print("\n2. Getting departures for a specific time")
    future_time = (datetime.now() + timedelta(hours=1)).strftime('%H:%M')
    print(f"  Requesting departures around {future_time}")
    
    time_departures = get_departure_monitor(stop_id, time=future_time, max_results=3)
    if time_departures:
        print(f"  Found {len(time_departures)} departures")
        
        if len(time_departures) > 0:
            # Show the time of the first departure
            first_dep = time_departures[0]
            print(f"  First departure at: {first_dep.get('local_departure_time', 'N/A')}")
    
    # Example 3: Filter by transport mode
    print("\n3. Getting only train departures")
    train_departures = get_departure_monitor(stop_id, mot_type=1, max_results=3)  # 1 = Train
    
    if train_departures:
        print(f"  Found {len(train_departures)} train departures")
        
        # Show destinations
        if train_departures:
            print("\n  Train destinations:")
            for i, departure in enumerate(train_departures[:3], 1):
                route = departure.get('route_number', 'N/A')
                dest = departure.get('destination', 'N/A')
                time = departure.get('local_departure_time', 'N/A')
                print(f"    {i}. {route} to {dest} at {time}")


def main():
    """Main demo function."""
    parser = argparse.ArgumentParser(description='Transport NSW API Demo')
    parser.add_argument('--stops', action='store_true', help='Run stops demo only')
    parser.add_argument('--alerts', action='store_true', help='Run alerts demo only')
    parser.add_argument('--departures', action='store_true', help='Run departures demo only')
    args = parser.parse_args()
    
    # Check if API key is set
    if not os.environ.get('OPEN_TRANSPORT_API_KEY'):
        print("Error: OPEN_TRANSPORT_API_KEY environment variable not set.")
        print("Please set it using:")
        print("  export OPEN_TRANSPORT_API_KEY=your_api_key")
        return
    
    print("\nTransport NSW API Demo")
    print("=====================")
    print("This script demonstrates the main functionality of the Transport NSW API wrapper.")
    
    # Run demos based on arguments
    run_all = not (args.stops or args.alerts or args.departures)
    
    if run_all or args.stops:
        find_stops_demo()
    
    if run_all or args.alerts:
        get_alerts_demo()
    
    if run_all or args.departures:
        monitor_departures_demo()
    
    print("\n" + "="*80)
    print(" DEMO COMPLETE ".center(80, "="))
    print("="*80)


if __name__ == "__main__":
    main()
