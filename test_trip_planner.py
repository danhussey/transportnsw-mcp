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

def test_trip_request(origin, destination=None, description=""):
    """Test the trip planner API with the given origin and destination."""
    print(f"\n{'='*80}")
    print(f"Testing trip from: {origin}" + 
          (f" to {destination}" if destination else "") + 
          (f" ({description})" if description else ""))
    print(f"{'='*80}")
    
    try:
        # If no destination is provided, use a common destination (Town Hall)
        if not destination:
            destination = "200070"  # Town Hall Station
        
        # Call the trip request API with all required parameters
        api_response = api_instance.tfnsw_trip_request2(
            output_format=output_format,
            coord_output_format='EPSG:4326',  # Standard coordinate format
            dep_arr_macro='dep',              # Departure time (not arrival)
            type_origin='stop',               # Origin is a stop ID
            name_origin=origin,               # The origin stop ID
            type_destination='stop',          # Destination is a stop ID
            name_destination=destination,     # The destination stop ID
            version=api_version
        )
        
        if api_response:
            print(f"API Version: {api_response.version}")
            
            # Check for journeys
            if hasattr(api_response, 'journeys') and api_response.journeys:
                print(f"\nFound {len(api_response.journeys)} journeys:")
                for i, journey in enumerate(api_response.journeys[:3]):  # Show first 3 journeys
                    print(f"\nJourney {i+1}:")
                    
                    # Display journey info
                    if hasattr(journey, 'legs'):
                        print(f"  Number of legs: {len(journey.legs)}")
                        for j, leg in enumerate(journey.legs):
                            print(f"  Leg {j+1}:")
                            
                            # Display transportation info
                            if hasattr(leg, 'transportation'):
                                trans = leg.transportation
                                if hasattr(trans, 'product') and hasattr(trans.product, 'name'):
                                    print(f"    Mode: {trans.product.name}")
                                if hasattr(trans, 'number'):
                                    print(f"    Line: {trans.number}")
                                if hasattr(trans, 'destination') and hasattr(trans.destination, 'name'):
                                    print(f"    Destination: {trans.destination.name}")
                            
                            # Display time info
                            if hasattr(leg, 'origin') and hasattr(leg.origin, 'departure_time_planned'):
                                print(f"    Departure: {leg.origin.departure_time_planned}")
                            if hasattr(leg, 'destination') and hasattr(leg.destination, 'arrival_time_planned'):
                                print(f"    Arrival: {leg.destination.arrival_time_planned}")
            else:
                print("\nNo journeys found.")
            
            # Print full response for debugging
            print("\nFull response as dictionary:")
            pp = pprint.PrettyPrinter(indent=2)
            pp.pprint(api_response.to_dict())
            
            return api_response
        else:
            print("No response from the API.")
            return None
    except ApiException as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None

# Test with various stop IDs
# Central Station
test_trip_request("200060", description="Central Station global ID")

# Try a different format of stop ID
test_trip_request("10111010", description="Central Station stop ID")

# Try the original stop ID from the user
test_trip_request("10111101-0-X1", description="User provided stop ID")

# Try a bus stop ID
test_trip_request("209516", description="Town Hall Station, Park St, Stand H")
