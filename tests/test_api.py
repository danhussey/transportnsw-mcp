import pytest
import time
from datetime import datetime
import swagger_client
from swagger_client.rest import ApiException
from api import find_transport_stops, get_transport_alerts, get_departure_monitor, api_instance, output_format, coord_output_format, incl_filter, api_version

# Test coordinates (Central Station, Sydney)
CENTRAL_STATION_COORD = '151.206290:-33.884080:EPSG:4326'

class TestCoordinateAPI:
    """Test suite for Transport NSW Coordinate API functionality."""
    
    def test_bus_stop_retrieval(self):
        """Test finding bus stops around a location."""
        bus_stops = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=500)
        
        # Verify response structure
        assert bus_stops is not None
        assert hasattr(bus_stops, 'locations')
        assert len(bus_stops.locations) > 0
        
        # Verify location properties
        for location in bus_stops.locations[:5]:
            assert hasattr(location, 'name')
            assert hasattr(location, 'id')
            assert hasattr(location, 'type')
            assert hasattr(location, 'coord')
    
    def test_poi_retrieval(self):
        """Test finding points of interest around a location."""
        poi_locations = find_transport_stops(CENTRAL_STATION_COORD, stop_type='POI_POINT', radius=500)
        
        # Verify response structure
        assert poi_locations is not None
        assert hasattr(poi_locations, 'locations')
        
        # If POIs are found, verify their properties
        if poi_locations.locations:
            for location in poi_locations.locations[:5]:
                assert hasattr(location, 'name')
                assert hasattr(location, 'id')
                assert hasattr(location, 'type')
                assert hasattr(location, 'coord')
                
        # Verify location types are valid if POIs exist
        if poi_locations.locations:
            location = poi_locations.locations[0]
            assert location.type == 'poi'  # POIs should have type 'poi'
    
    def test_response_time(self):
        """Test API response time."""
        start_time = time.time()
        bus_stops = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=500)
        elapsed = time.time() - start_time
        
        # API should respond within a reasonable time (5 seconds)
        assert elapsed < 5, f"API response took too long: {elapsed:.2f} seconds"
        assert bus_stops is not None
    
    def test_invalid_stop_type(self):
        """Test that GIS_POINT returns an error as expected."""
        with pytest.raises(Exception) as excinfo:
            api_instance.tfnsw_coord_request(
                output_format=output_format,
                coord=CENTRAL_STATION_COORD,
                coord_output_format=coord_output_format,
                incl_filter=incl_filter,
                type_1='GIS_POINT',
                radius_1=500,
                version=api_version
            )
        
        # Verify that an exception was raised
        assert excinfo.value is not None
    
    def test_radius_parameter(self):
        """Test that different radius values affect the number of results."""
        # Small radius should return fewer results
        small_radius_results = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=100)
        
        # Larger radius should return more results
        large_radius_results = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=1000)
        
        # Only compare if both requests were successful
        if small_radius_results and large_radius_results:
            if hasattr(small_radius_results, 'locations') and hasattr(large_radius_results, 'locations'):
                # The larger radius should generally return more results
                # Note: This is not guaranteed but is likely in an urban area
                assert len(small_radius_results.locations) <= len(large_radius_results.locations)
    
    def test_different_location(self):
        """Test API with a different location."""
        # Coordinates for Sydney Opera House
        opera_house_coord = '151.214897:-33.857438:EPSG:4326'
        
        opera_house_stops = find_transport_stops(opera_house_coord, stop_type='BUS_POINT', radius=500)
        assert opera_house_stops is not None
        assert hasattr(opera_house_stops, 'locations')


class TestTransportAlerts:
    """Test suite for Transport NSW Alert API functionality."""
    
    def test_basic_alert_retrieval(self):
        """Test basic alert retrieval with default parameters."""
        alerts = get_transport_alerts()
        assert alerts is not None
        assert hasattr(alerts, 'version')
        assert alerts.version == api_version
        assert hasattr(alerts, 'timestamp')
        assert hasattr(alerts, 'infos')
    
    def test_filtered_alert_retrieval(self):
        """Test alert retrieval with mode of transport filter."""
        # Test for train alerts (mot_type=1)
        train_alerts = get_transport_alerts(mot_type=1)
        assert train_alerts is not None
        assert hasattr(train_alerts, 'version')
        assert train_alerts.version == api_version
        
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
    
    def test_alerts_performance(self):
        """Test API response time."""
        start_time = time.time()
        alerts = get_transport_alerts()
        elapsed = time.time() - start_time
        
        # API should respond within a reasonable time (5 seconds)
        assert elapsed < 5, f"API response took too long: {elapsed:.2f} seconds"


class TestDepartureMonitor:
    """Test suite for Transport NSW Departure Monitor API functionality."""
    
    # Test stop ID for Central Station
    CENTRAL_STATION_ID = "200060"  # Central Station global ID
    
    def test_basic_departure_retrieval(self):
        """Test basic departure monitor retrieval with default parameters."""
        departures = get_departure_monitor(self.CENTRAL_STATION_ID)
        
        # Verify response structure
        assert departures is not None
        assert isinstance(departures, list), "Response should be a list of departures"
        
        # Check departure structure if any are returned
        if len(departures) > 0:
            # Verify the structure of a departure object
            departure = departures[0]
            assert isinstance(departure, dict), "Each departure should be a dictionary"
            assert 'stop_name' in departure, "Departure should have a stop_name"
            assert 'local_departure_time' in departure, "Departure should have a local_departure_time"
    
    def test_mot_type_filter(self):
        """Test departure retrieval with mode of transport filter."""
        # Test for train departures (mot_type=1)
        train_departures = get_departure_monitor(self.CENTRAL_STATION_ID, mot_type=1)
        assert train_departures is not None
        assert isinstance(train_departures, list), "Response should be a list of departures"
    
    def test_date_parameter(self):
        """Test departure retrieval with specific date."""
        # Test for departures on a specific date
        tomorrow = (datetime.now().date().replace(day=datetime.now().day + 1)).strftime('%d-%m-%Y')
        date_departures = get_departure_monitor(self.CENTRAL_STATION_ID, date=tomorrow)
        assert date_departures is not None
        assert isinstance(date_departures, list), "Response should be a list of departures"
    
    def test_time_parameter(self):
        """Test departure retrieval with specific time."""
        # Test for departures at a specific time
        time_departures = get_departure_monitor(self.CENTRAL_STATION_ID, time="12:00")
        assert time_departures is not None
        assert isinstance(time_departures, list), "Response should be a list of departures"
    
    def test_multiple_filters(self):
        """Test departure retrieval with multiple filters."""
        # Test for train departures with date and time
        filtered_departures = get_departure_monitor(
            self.CENTRAL_STATION_ID, 
            mot_type=1,
            time="12:00"
        )
        assert filtered_departures is not None
        assert isinstance(filtered_departures, list), "Response should be a list of departures"
    
    def test_invalid_stop_id(self):
        """Test behavior with invalid stop ID."""
        invalid_departures = get_departure_monitor("INVALID_ID")
        # The API might return an empty list or None for invalid IDs
        if invalid_departures is not None:
            # If a response is returned, it should be a list (possibly empty)
            assert isinstance(invalid_departures, list), "Response should be a list"
    
    def test_response_time(self):
        """Test API response time."""
        start_time = time.time()
        departures = get_departure_monitor(self.CENTRAL_STATION_ID)
        elapsed = time.time() - start_time
        
        # API should respond within a reasonable time (5 seconds)
        assert elapsed < 5, f"API response took too long: {elapsed:.2f} seconds"
        assert departures is not None


if __name__ == "__main__":
    pytest.main(["-v", "test_api.py"])
