import pytest
import time
from api import find_transport_stops, api_instance, output_format, coord_output_format, incl_filter

class TestCoordinateAPI:
    """Test suite for Transport NSW Coordinate API functionality."""
    
    # Central Station coordinates for testing
    test_coord = '151.206290:-33.884080:EPSG:4326'
    
    def test_bus_stop_retrieval(self):
        """Test finding bus stops around a location."""
        bus_stops = find_transport_stops(self.test_coord, stop_type='BUS_POINT', radius=500)
        
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
        poi_locations = find_transport_stops(self.test_coord, stop_type='POI_POINT', radius=500)
        
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
    
    def test_response_time(self):
        """Test API response time."""
        start_time = time.time()
        bus_stops = find_transport_stops(self.test_coord, stop_type='BUS_POINT', radius=500)
        elapsed = time.time() - start_time
        
        # API should respond within a reasonable time (5 seconds)
        assert elapsed < 5, f"API response took too long: {elapsed:.2f} seconds"
        assert bus_stops is not None
    
    def test_invalid_stop_type(self):
        """Test that GIS_POINT returns an error as expected."""
        with pytest.raises(Exception) as excinfo:
            api_instance.tfnsw_coord_request(
                output_format=output_format,
                coord=self.test_coord,
                coord_output_format=coord_output_format,
                incl_filter=incl_filter,
                type_1='GIS_POINT',
                radius_1=500,
                version='10.2.1.42'
            )
        
        # Verify that an exception was raised
        assert excinfo.value is not None
    
    def test_radius_parameter(self):
        """Test that different radius values affect the number of results."""
        # Small radius should return fewer results
        small_radius_results = find_transport_stops(self.test_coord, stop_type='BUS_POINT', radius=100)
        
        # Larger radius should return more results
        large_radius_results = find_transport_stops(self.test_coord, stop_type='BUS_POINT', radius=1000)
        
        # Only compare if both requests were successful
        if small_radius_results and large_radius_results:
            if hasattr(small_radius_results, 'locations') and hasattr(large_radius_results, 'locations'):
                # The larger radius should generally return more results
                # Note: This is not guaranteed but is likely in an urban area
                assert len(small_radius_results.locations) <= len(large_radius_results.locations)

if __name__ == "__main__":
    pytest.main(["-v", "test_api.py"])
