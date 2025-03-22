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
api_version = '10.2.1.42'  # API version

def get_departure_monitor(stop_id, date=None, mot_type=None):
    """
    Get departure monitor information for a specific stop.
    
    Args:
        stop_id (str): Stop ID or global stop ID
        date (str, optional): Date in DD-MM-YYYY format. Defaults to today's date.
        mot_type (int, optional): Mode of transport type filter.
        
    Returns:
        API response containing departure information
    """
    # Set default date to today if not provided
    if date is None:
        date = datetime.now().strftime('%d-%m-%Y')
    
    try:
        # Based on the error message, tfnsw_dm_request requires these parameters:
        # output_format, coord_output_format, type_dm, name_dm
        
        # Required parameters
        coord_output_format = 'EPSG:4326'  # Standard coordinate format
        type_dm = 'stop'  # Assuming 'stop' is the type for departure monitor
        
        # Try with the basic required parameters
        print(f"Trying to get departure information for stop ID: {stop_id}")
        
        try:
            api_response = api_instance.tfnsw_dm_request(
                output_format=output_format,
                coord_output_format=coord_output_format,
                type_dm=type_dm,
                name_dm=stop_id,
                version=api_version
            )
            return api_response
        except Exception as e1:
            print(f"First attempt failed: {e1}")
            
            # Try with different type_dm values
            types_to_try = ['any', 'stop', 'poi', 'coord']
            for type_val in types_to_try:
                if type_val == type_dm:  # Skip the one we already tried
                    continue
                    
                try:
                    print(f"Trying with type_dm={type_val}")
                    api_response = api_instance.tfnsw_dm_request(
                        output_format=output_format,
                        coord_output_format=coord_output_format,
                        type_dm=type_val,
                        name_dm=stop_id,
                        version=api_version
                    )
                    return api_response
                except Exception as e:
                    print(f"  Failed with type_dm={type_val}: {e}")
            
            # Try the trip request endpoint as a fallback
            try:
                print("\nTrying trip request2 endpoint...")
                api_response = api_instance.tfnsw_trip_request2(
                    output_format=output_format,
                    origin=stop_id,
                    version=api_version
                )
                return api_response
            except Exception as e4:
                print(f"Trip request2 attempt failed: {e4}")
                
            # Last resort: try to list available methods
            print("\nAvailable API methods:")
            for method in dir(api_instance):
                if method.startswith('tfnsw_') and callable(getattr(api_instance, method)):
                    print(f"  {method}")
            
            return None
    except ApiException as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None

# Test with the provided stop ID
stop_id = "10111101-0-X1"
result = get_departure_monitor(stop_id)

# Print the result in a readable format
if result:
    print("\nAPI Response:")
    print(f"Type: {type(result)}")
    
    # Print all top-level attributes
    print("\nTop-level attributes:")
    for attr in dir(result):
        if not attr.startswith('_') and attr not in ['to_dict', 'swagger_types', 'attribute_map']:
            value = getattr(result, attr)
            if value is not None:
                print(f"  {attr}: {value}")
    
    # Pretty print the dictionary representation
    print("\nFull response as dictionary:")
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(result.to_dict())
else:
    print("No result returned from the API.")
