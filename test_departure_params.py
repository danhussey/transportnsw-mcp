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

def test_departure_params(stop_id, description=""):
    """Test departure monitor with different parameter combinations."""
    print(f"\n{'='*80}")
    print(f"Testing departure monitor for stop ID: {stop_id}" + (f" ({description})" if description else ""))
    print(f"{'='*80}")
    
    # Try with additional parameters
    try:
        # Try with itdDate and itdTime parameters
        now = datetime.now()
        itd_date = now.strftime('%Y%m%d')  # Format: YYYYMMDD
        itd_time = now.strftime('%H%M')    # Format: HHMM
        
        print(f"Trying with itdDate={itd_date} and itdTime={itd_time}")
        api_response = api_instance.tfnsw_dm_request(
            output_format=output_format,
            coord_output_format=coord_output_format,
            type_dm='stop',
            name_dm=stop_id,
            itdDate=itd_date,
            itdTime=itd_time,
            version=api_version
        )
        
        if api_response and hasattr(api_response, 'stop_events') and api_response.stop_events:
            print(f"Success! Found {len(api_response.stop_events)} departures.")
            return api_response
        else:
            print("No departure events found with itdDate and itdTime parameters.")
        
        # Try with mode parameter
        print("Trying with mode=direct")
        api_response = api_instance.tfnsw_dm_request(
            output_format=output_format,
            coord_output_format=coord_output_format,
            type_dm='stop',
            name_dm=stop_id,
            mode='direct',
            version=api_version
        )
        
        if api_response and hasattr(api_response, 'stop_events') and api_response.stop_events:
            print(f"Success! Found {len(api_response.stop_events)} departures.")
            return api_response
        else:
            print("No departure events found with mode=direct parameter.")
        
        # Try with ptOptionsActive parameter
        print("Trying with ptOptionsActive=1")
        api_response = api_instance.tfnsw_dm_request(
            output_format=output_format,
            coord_output_format=coord_output_format,
            type_dm='stop',
            name_dm=stop_id,
            ptOptionsActive=1,
            version=api_version
        )
        
        if api_response and hasattr(api_response, 'stop_events') and api_response.stop_events:
            print(f"Success! Found {len(api_response.stop_events)} departures.")
            return api_response
        else:
            print("No departure events found with ptOptionsActive=1 parameter.")
        
        # Try with departureMonitorMacro parameter
        print("Trying with departureMonitorMacro=true")
        api_response = api_instance.tfnsw_dm_request(
            output_format=output_format,
            coord_output_format=coord_output_format,
            type_dm='stop',
            name_dm=stop_id,
            departureMonitorMacro=True,
            version=api_version
        )
        
        if api_response and hasattr(api_response, 'stop_events') and api_response.stop_events:
            print(f"Success! Found {len(api_response.stop_events)} departures.")
            return api_response
        else:
            print("No departure events found with departureMonitorMacro=true parameter.")
        
        # Try with a different type_dm
        print("Trying with type_dm=any")
        api_response = api_instance.tfnsw_dm_request(
            output_format=output_format,
            coord_output_format=coord_output_format,
            type_dm='any',
            name_dm=stop_id,
            version=api_version
        )
        
        if api_response and hasattr(api_response, 'stop_events') and api_response.stop_events:
            print(f"Success! Found {len(api_response.stop_events)} departures.")
            return api_response
        else:
            print("No departure events found with type_dm=any parameter.")
        
        # If all attempts fail, print the last response for debugging
        print("\nFull response from last attempt:")
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(api_response.to_dict())
        
        return api_response
    except ApiException as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None

# Test with known valid stop IDs
test_departure_params("200060", "Central Station")
test_departure_params("200070", "Town Hall Station")
test_departure_params("200080", "Wynyard Station")
test_departure_params("200010", "Circular Quay Station")
