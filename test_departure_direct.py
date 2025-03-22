import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import json
import pprint

# Load environment variables
load_dotenv()
API_KEY = os.getenv('OPEN_TRANSPORT_API_KEY')

# API endpoint
API_ENDPOINT = 'https://api.transport.nsw.gov.au/v1/tp/departure_mon'

def get_departure_monitor(stop_id, date=None, time=None):
    """
    Get departure monitor information for a specific stop using direct HTTP request.
    
    Args:
        stop_id (str): Stop ID
        date (str, optional): Date in YYYYMMDD format. Defaults to today.
        time (str, optional): Time in HHMM format. Defaults to now.
        
    Returns:
        dict: API response containing departure information
    """
    # Set default date and time to now if not provided
    now = datetime.now()
    
    if date is None:
        date = now.strftime('%Y%m%d')
    
    if time is None:
        time = now.strftime('%H%M')
    
    # Set up the request parameters exactly as in the documentation
    params = {
        'outputFormat': 'rapidJSON',
        'coordOutputFormat': 'EPSG:4326',
        'mode': 'direct',
        'type_dm': 'stop',
        'name_dm': stop_id,
        'depArrMacro': 'dep',
        'itdDate': date,
        'itdTime': time,
        'TfNSWDM': 'true'
    }
    
    # Set up the headers with the API key
    headers = {
        'Authorization': f'apikey {API_KEY}'
    }
    
    # Make the request
    print(f"Making request to {API_ENDPOINT} with parameters:")
    for key, value in params.items():
        print(f"  {key}: {value}")
    
    response = requests.get(API_ENDPOINT, params=params, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        print(f"Request successful! Status code: {response.status_code}")
        
        # Parse the JSON response
        try:
            data = response.json()
            return data
        except json.JSONDecodeError:
            print("Error decoding JSON response")
            print(f"Response text: {response.text[:500]}...")  # Print first 500 chars
            return None
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response text: {response.text[:500]}...")  # Print first 500 chars
        return None

def test_stop_id(stop_id, description=""):
    """Test a specific stop ID and print the results."""
    print(f"\n{'='*80}")
    print(f"Testing stop ID: {stop_id}" + (f" ({description})" if description else ""))
    print(f"{'='*80}")
    
    result = get_departure_monitor(stop_id)
    
    if result:
        print(f"\nAPI Response:")
        
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
        
        # Print full response for debugging
        print("\nFull response as dictionary:")
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(result)
    else:
        print("No result returned from the API.")

# Test with the stop ID from the documentation
test_stop_id("10101331", "Domestic Airport Station (from documentation)")

# Test with other stop IDs
test_stop_id("200060", "Central Station global ID")
test_stop_id("200070", "Town Hall Station")
test_stop_id("200080", "Wynyard Station")
test_stop_id("200010", "Circular Quay Station")
