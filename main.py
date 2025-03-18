from __future__ import print_function
from pprint import pprint

# Import from centralized API module
from api import get_transport_alerts

# Example usage of the API
def main():
    """
    Main function to demonstrate the Transport NSW Alerts API.
    """
    print("\n=== Transport NSW Alerts API Demo ===\n")
    
    # Example 1: Get alerts for a specific date
    date = '18-03-2025'
    print(f"\n1. Getting alerts for {date}:")
    alerts = get_transport_alerts(date=date)
    
    if alerts:
        print(f"  Retrieved alerts successfully!")
        print(f"  Version: {alerts.version}")
        print(f"  Timestamp: {alerts.timestamp}")
        
        # Check if there are any alerts
        if hasattr(alerts.infos, 'info') and alerts.infos.info:
            print(f"  Number of alerts: {len(alerts.infos.info)}")
            
            # Print first alert as an example
            first_alert = alerts.infos.info[0]
            print("\n  Example alert:")
            print(f"    Title: {getattr(first_alert, 'title', 'N/A')}")
            print(f"    Priority: {getattr(first_alert, 'priority', 'N/A')}")
        else:
            print("  No alerts found for this date.")
    else:
        print("  Failed to retrieve alerts.")
    
    # Example 2: Get train alerts only
    print("\n2. Getting train alerts only:")
    train_alerts = get_transport_alerts(date=date, mot_type=1)
    
    if train_alerts and hasattr(train_alerts.infos, 'info') and train_alerts.infos.info:
        print(f"  Retrieved {len(train_alerts.infos.info)} train alerts.")
    else:
        print("  No train alerts found or error occurred.")


if __name__ == "__main__":
    main()