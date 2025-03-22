from api import get_next_departure
import json

# Test with the provided stop ID
stop_id = "10111101-0-X1"
result = get_next_departure(stop_id)

# Print the result in a readable format
if result:
    print(f"API Version: {result.version}")
    print(f"Timestamp: {result.timestamp}")
    
    if hasattr(result, 'infos') and result.infos:
        # Handle the infos object which might not be a standard list
        if hasattr(result.infos, 'affected'):
            print("\nAffected information:")
            affected = result.infos.affected
            if affected:
                for i, item in enumerate(affected):
                    print(f"\nAffected Item {i+1}:")
                    for attr in dir(item):
                        if not attr.startswith('_') and attr not in ['to_dict', 'swagger_types', 'attribute_map']:
                            value = getattr(item, attr)
                            if value is not None:
                                print(f"  {attr}: {value}")
        
        # Try to access any other attributes of infos
        print("\nInfos attributes:")
        for attr in dir(result.infos):
            if not attr.startswith('_') and attr not in ['to_dict', 'swagger_types', 'attribute_map', 'affected']:
                value = getattr(result.infos, attr)
                if value is not None:
                    print(f"  {attr}: {value}")
    else:
        print("\nNo information items found.")
    
    # Print all top-level attributes of the result object
    print("\nAll available top-level attributes:")
    for attr in dir(result):
        if not attr.startswith('_') and attr not in ['to_dict', 'swagger_types', 'attribute_map', 'infos', 'version', 'timestamp']:
            value = getattr(result, attr)
            if value is not None:
                print(f"  {attr}: {value}")
else:
    print("No result returned from the API.")
