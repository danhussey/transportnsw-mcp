import pytest
import time
from demo import get_transport_alerts, print_alerts

class TestTransportAlerts:
    """Test suite for Transport NSW Alert API functionality."""
    
    def test_basic_alert_retrieval(self):
        """Test basic alert retrieval with default parameters."""
        alerts = get_transport_alerts()
        assert alerts is not None
        assert hasattr(alerts, 'version')
        assert alerts.version == '10.2.1.42'
        assert hasattr(alerts, 'timestamp')
        assert hasattr(alerts, 'infos')
    
    def test_filtered_alert_retrieval(self):
        """Test alert retrieval with mode of transport filter."""
        # Test for train alerts (mot_type=1)
        train_alerts = get_transport_alerts(mot_type=1)
        assert train_alerts is not None
        assert hasattr(train_alerts, 'version')
        assert train_alerts.version == '10.2.1.42'
        
        # Test for bus alerts (mot_type=5)
        bus_alerts = get_transport_alerts(mot_type=5)
        assert bus_alerts is not None
        assert hasattr(bus_alerts, 'version')
    
    def test_date_filtered_alert_retrieval(self):
        """Test alert retrieval with date filter."""
        # Test for alerts on a specific date
        future_date = '20-03-2025'
        date_alerts = get_transport_alerts(date=future_date)
        assert date_alerts is not None
        assert hasattr(date_alerts, 'version')
    
    def test_multiple_filters(self):
        """Test alert retrieval with multiple filters."""
        # Test for train alerts on a specific date
        future_date = '20-03-2025'
        filtered_alerts = get_transport_alerts(date=future_date, mot_type=1)
        assert filtered_alerts is not None
        assert hasattr(filtered_alerts, 'version')
    
    def test_response_structure(self):
        """Test the structure of the API response."""
        alerts = get_transport_alerts()
        assert hasattr(alerts, 'infos')
        
        # The structure might not have 'info' attribute if there are no alerts
        # Instead, check that the response has a valid structure overall
        assert alerts.infos is not None
    
    def test_performance(self):
        """Test API response time."""
        start_time = time.time()
        alerts = get_transport_alerts()
        elapsed = time.time() - start_time
        
        # API should respond within a reasonable time (5 seconds)
        assert elapsed < 5, f"API response took too long: {elapsed:.2f} seconds"
    
    def test_print_alerts_function(self, capsys):
        """Test the print_alerts function with various inputs."""
        # Test with None
        print_alerts(None)
        captured = capsys.readouterr()
        assert "No alerts data available" in captured.out
        
        # Test with actual alerts
        alerts = get_transport_alerts()
        print_alerts(alerts)
        captured = capsys.readouterr()
        assert "Transport NSW Alerts" in captured.out
        assert f"Version: {alerts.version}" in captured.out

if __name__ == "__main__":
    pytest.main(["-v", "test_alerts.py"])
