# Transport NSW API Client (MCP Implementation)

A Claude MCP for interacting with the Transport NSW API.

## About

This project implements a Model Context Protocol (MCP) service for parts of Transport NSW's API.

## Setup

1. Clone this repository
2. Install dependencies using uv (fast Python package manager):
   ```bash
   uv venv
   uv sync
   ```
3. Create a `.env` file with your API key:
   ```
   OPEN_TRANSPORT_API_KEY=your_api_key_here
   ```
4. (Optional) Run the MCP Inspector:
   ```bash
   uv run mcp dev api.py
   ```
And visit the server at http://localhost:5173 (port might be different).

## Features

- **Coordinate API**: Find transport stops and points of interest around a location
- **Alerts API**: Get information about transport alerts and disruptions
- **MCP Implementation**: Structured as a Model Context Protocol service

## Usage Examples

MCP Examples coming soon. Standard Python examples below:

### Find Transport Stops

```python
from api import find_transport_stops

# Central Station coordinates
central_station = '151.206290:-33.884080:EPSG:4326'

# Find bus stops within 500m of Central Station
bus_stops = find_transport_stops(central_station, stop_type='BUS_POINT', radius=500)

# Find points of interest
pois = find_transport_stops(central_station, stop_type='POI_POINT', radius=500)
```

### Get Transport Alerts

```python
from api import get_transport_alerts

# Get all current alerts
alerts = get_transport_alerts()

# Get alerts for a specific date
date_alerts = get_transport_alerts(date='01-01-2025')

# Get train alerts only (mot_type=1)
train_alerts = get_transport_alerts(mot_type=1)
```

## Demo Scripts

- `coord_demo.py`: Demonstrates finding transport stops around Central Station
- `demo.py`: Shows how to use the Transport NSW Coordinate API
- `main.py`: Demonstrates the Transport NSW Alerts API

## Testing

### Local Testing

Run tests locally with pytest:

```bash
uv run pytest test_api.py -v
```

### Continuous Integration

Tests automatically run on GitHub Actions for every push and pull request to the main branch. The workflow:

1. Sets up Python 3.10
2. Installs uv and project dependencies
3. Runs tests with coverage reporting

To use this feature:

1. Add your `OPEN_TRANSPORT_API_KEY` as a GitHub repository secret
2. Push your code to GitHub

## MCP Integration

This project follows the Model Context Protocol specification, allowing AI models to access Transport NSW data through a standardized interface.

## Package Management

This project uses uv, a modern Python package manager written in Rust. Dependencies are managed through:

- `pyproject.toml`: Defines project dependencies
- `uv.lock`: Locks dependency versions for reproducible environments
- Local dependencies (like swagger-client) are referenced in the [tool.uv.sources] section