from __future__ import print_function
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import os
from datetime import datetime

def get_transport_alerts(date=None, mot_type=None, stop_id=None, line_number=None, operator_id=None):
    """
    Get transport alerts from the Transport NSW API.
    
    Args:
        date (str, optional): Date in DD-MM-YYYY format. Defaults to today's date.
        mot_type (int, optional): Mode of transport type filter. Options:
            1: Train
            2: Metro
            4: Light Rail
            5: Bus
            7: Coach
            9: Ferry
            11: School Bus
        stop_id (str, optional): Stop ID or global stop ID to filter by.
        line_number (str, optional): Line number to filter by (e.g., '020T1').
        operator_id (str, optional): Operator ID to filter by.
    
    Returns:
        dict: API response containing alerts information
    """
    # Load environment variables
    load_dotenv()
    
    # Configure API key authorization
    configuration = swagger_client.Configuration()
    configuration.api_key['Authorization'] = os.getenv('OPEN_TRANSPORT_API_KEY')
    configuration.api_key_prefix['Authorization'] = 'apikey'
    
    # Create API instance
    api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
    
    # Set default date to today if not provided
    if date is None:
        date = datetime.now().strftime('%d-%m-%Y')
    
    # Required parameter
    output_format = 'rapidJSON'
    
    # Optional parameters
    kwargs = {
        'filter_date_valid': date,
        'version': '10.2.1.42'
    }
    
    # Add optional filters if provided
    if mot_type is not None:
        kwargs['filter_mot_type'] = mot_type
    
    if stop_id is not None:
        kwargs['itd_l_pxx_sel_stop'] = stop_id
    
    if line_number is not None:
        kwargs['itd_l_pxx_sel_line'] = line_number
    
    if operator_id is not None:
        kwargs['itd_l_pxx_sel_operator'] = operator_id
    
    try:
        # Call the API
        api_response = api_instance.tfnsw_addinfo_request(output_format, **kwargs)
        return api_response
    except ApiException as e:
        print(f"Exception when calling Transport NSW API: {e}\n")
        return None


def print_alerts(alerts):
    """
    Print alerts in a readable format.
    
    Args:
        alerts (dict): API response from get_transport_alerts()
    """
    if alerts is None:
        print("No alerts data available.")
        return
    
    print(f"Transport NSW Alerts - Version: {alerts.version}")
    print(f"Timestamp: {alerts.timestamp}")
    
    # Check if there are any alerts
    if not hasattr(alerts.infos, 'info') or not alerts.infos.info:
        print("\nNo alerts found for the specified criteria.")
        return
    
    print("\nAlerts:")
    
    # Process each alert
    for info in alerts.infos.info:
        print(f"\n{'-'*50}")
        
        # Use safe attribute access with getattr
        print(f"ID: {getattr(info, 'id', 'N/A')}")
        print(f"Title: {getattr(info, 'title', 'N/A')}")
        print(f"Description: {getattr(info, 'description', 'N/A')}")
        print(f"Priority: {getattr(info, 'priority', 'N/A')}")
        print(f"Valid From: {getattr(info, 'validFrom', 'N/A')}")
        print(f"Valid To: {getattr(info, 'validTo', 'N/A')}")
        
        # Print affected modes of transport
        if hasattr(info, 'affectedMOTs') and info.affectedMOTs:
            print("\nAffected Modes of Transport:")
            for mot in info.affectedMOTs:
                print(f"  - {getattr(mot, 'name', 'N/A')} (Type: {getattr(mot, 'type', 'N/A')})")


def get_alerts_cli():
    """
    Command-line interface for getting transport alerts.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Get Transport NSW alerts')
    parser.add_argument('--date', type=str, help='Date in DD-MM-YYYY format (default: today)')
    parser.add_argument('--mode', type=int, choices=[1, 2, 4, 5, 7, 9, 11], 
                        help='Mode of transport: 1=Train, 2=Metro, 4=Light Rail, 5=Bus, 7=Coach, 9=Ferry, 11=School Bus')
    parser.add_argument('--stop', type=str, help='Stop ID or global stop ID')
    parser.add_argument('--line', type=str, help='Line number (e.g., 020T1)')
    parser.add_argument('--operator', type=str, help='Operator ID')
    parser.add_argument('--raw', action='store_true', help='Print raw API response')
    
    args = parser.parse_args()
    
    # Get alerts based on provided arguments
    alerts = get_transport_alerts(
        date=args.date,
        mot_type=args.mode,
        stop_id=args.stop,
        line_number=args.line,
        operator_id=args.operator
    )
    
    # Print the results
    if args.raw:
        pprint(alerts)
    else:
        print_alerts(alerts)


def test_api_responses():
    """
    Test function to verify API responses and error handling.
    This helps diagnose issues with the Transport NSW API.
    """
    import json
    import time
    
    print("\n=== Transport NSW API Test ===\n")
    
    # Test 1: Basic alert retrieval
    print("Test 1: Basic alert retrieval")
    try:
        start_time = time.time()
        alerts = get_transport_alerts()
        elapsed = time.time() - start_time
        print(f"  Status: {'✓ Success' if alerts else '✗ Failed'}")
        print(f"  Response time: {elapsed:.2f} seconds")
        print(f"  Version: {getattr(alerts, 'version', 'N/A')}")
        print(f"  Has alerts: {hasattr(alerts, 'infos') and hasattr(alerts.infos, 'info') and bool(alerts.infos.info)}")
    except Exception as e:
        print(f"  Error: {str(e)}")
    
    # Test 2: Filtered alert retrieval (train only)
    print("\nTest 2: Filtered alert retrieval (train only)")
    try:
        start_time = time.time()
        train_alerts = get_transport_alerts(mot_type=1)
        elapsed = time.time() - start_time
        print(f"  Status: {'✓ Success' if train_alerts else '✗ Failed'}")
        print(f"  Response time: {elapsed:.2f} seconds")
        print(f"  Version: {getattr(train_alerts, 'version', 'N/A')}")
    except Exception as e:
        print(f"  Error: {str(e)}")
    
    # Test 3: Future date alert retrieval
    print("\nTest 3: Future date alert retrieval")
    try:
        future_date = '20-03-2025'  # Two days in the future
        start_time = time.time()
        future_alerts = get_transport_alerts(date=future_date)
        elapsed = time.time() - start_time
        print(f"  Status: {'✓ Success' if future_alerts else '✗ Failed'}")
        print(f"  Response time: {elapsed:.2f} seconds")
        print(f"  Date requested: {future_date}")
    except Exception as e:
        print(f"  Error: {str(e)}")
    
    # Test 4: Invalid parameter test
    print("\nTest 4: Invalid parameter test")
    try:
        start_time = time.time()
        invalid_alerts = get_transport_alerts(mot_type=999)  # Invalid mode of transport
        elapsed = time.time() - start_time
        print(f"  Status: {'✓ Success' if invalid_alerts else '✗ Failed'}")
        print(f"  Response time: {elapsed:.2f} seconds")
    except Exception as e:
        print(f"  Status: ✓ Expected error")
        print(f"  Error: {str(e)}")
    
    print("\n=== Test Complete ===\n")


if __name__ == "__main__":
    import sys
    
    # If arguments are provided, use the CLI
    if len(sys.argv) > 1:
        # Check for test flag
        if sys.argv[1] == "--test":
            test_api_responses()
        else:
            get_alerts_cli()
    else:
        # Example usage
        print("\n1. Get all alerts for today:")
        alerts = get_transport_alerts()
        print_alerts(alerts)
        
        print("\n2. Get train alerts only:")
        train_alerts = get_transport_alerts(mot_type=1)
        print_alerts(train_alerts)
        
        print("\nTry running with command-line arguments for more options:")
        print("python demo.py --help")
        print("python demo.py --mode 1 --date 20-03-2025")
        print("python demo.py --stop 200060 --raw")
        print("python demo.py --test")