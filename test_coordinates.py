import pytest
import time
import swagger_client
from swagger_client.rest import ApiException
from dotenv import load_dotenv
import os
import sys

# Add the project root to the path to import from coord_demo
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from coord_demo import find_transport_stops

# Load environment variables and set up API client
load_dotenv()
API_KEY = os.getenv('OPEN_TRANSPORT_API_KEY')

# Configure API key authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = API_KEY
configuration.api_key_prefix['Authorization'] = 'apikey'

# Create API instance
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

# Test coordinates (Central Station, Sydney)
CENTRAL_STATION_COORD = '151.206290:-33.884080:EPSG:4326'


class TestCoordinateAPI:
    """Test suite for Transport NSW Coordinate API functionality."""
    
    def test_bus_stop_retrieval(self):
        """Test retrieval of bus stops around a location."""
        bus_stops = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=500)
        
        # Verify response structure
        assert bus_stops is not None
        assert hasattr(bus_stops, 'locations')
        assert len(bus_stops.locations) > 0
        
        # Verify location data
        location = bus_stops.locations[0]
        assert hasattr(location, 'name')
        assert hasattr(location, 'id')
        assert hasattr(location, 'type')
        assert hasattr(location, 'coord')
        
        # Verify location types are valid
        valid_types = ['poi', 'singlehouse', 'stop', 'platform', 'street', 
                      'locality', 'suburb', 'gisPoint', 'unknown']
        for loc in bus_stops.locations[:10]:
            assert loc.type in valid_types
    
    def test_poi_retrieval(self):
        """Test retrieval of points of interest around a location."""
        pois = find_transport_stops(CENTRAL_STATION_COORD, stop_type='POI_POINT', radius=500)
        
        # Verify response structure
        assert pois is not None
        assert hasattr(pois, 'locations')
        
        # Only proceed with further checks if POIs were found
        if len(pois.locations) > 0:
            # Verify location data
            location = pois.locations[0]
            assert hasattr(location, 'name')
            assert hasattr(location, 'id')
            assert hasattr(location, 'type')
            assert location.type == 'poi'  # POIs should have type 'poi'
    
    def test_gis_point_error(self):
        """Test that GIS_POINT parameter causes expected error."""
        with pytest.raises(ValueError) as excinfo:
            api_instance.tfnsw_coord_request(
                output_format='rapidJSON',
                coord=CENTRAL_STATION_COORD,
                coord_output_format='EPSG:4326',
                incl_filter=1,
                type_1='GIS_POINT',
                radius_1=500,
                version='10.2.1.42'
            )
        
        # Verify the error message
        error_msg = str(excinfo.value)
        assert "Invalid value for `type`" in error_msg
        assert "must be one of" in error_msg
    
    def test_performance(self):
        """Test API response time."""
        start_time = time.time()
        bus_stops = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=500)
        elapsed = time.time() - start_time
        
        # API should respond within a reasonable time (5 seconds)
        assert elapsed < 5, f"API response took too long: {elapsed:.2f} seconds"
    
    def test_radius_parameter(self):
        """Test that radius parameter affects the number of results."""
        # Get results with small radius
        small_radius = 100
        small_results = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=small_radius)
        
        # Get results with larger radius
        large_radius = 1000
        large_results = find_transport_stops(CENTRAL_STATION_COORD, stop_type='BUS_POINT', radius=large_radius)
        
        # Larger radius should return more or equal number of results
        assert len(large_results.locations) >= len(small_results.locations)
    
    def test_different_location(self):
        """Test API with a different location."""
        # Coordinates for Sydney Opera House
        opera_house_coord = '151.214897:-33.857438:EPSG:4326'
        
        opera_house_stops = find_transport_stops(opera_house_coord, stop_type='BUS_POINT', radius=500)
        assert opera_house_stops is not None
        assert hasattr(opera_house_stops, 'locations')


if __name__ == "__main__":
    pytest.main(["-v", "test_coordinates.py"])
