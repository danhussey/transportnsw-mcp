# Transport NSW API Client (MCP Implementation)

[![Tests](https://github.com/danhussey/transportnsw-mcp/actions/workflows/tests.yml/badge.svg)](https://github.com/danhussey/transportnsw-mcp/actions/workflows/tests.yml)

A Claude MCP for interacting with the Transport NSW API using direct HTTP requests.

## About

This project implements a Model Context Protocol (MCP) service for Transport NSW's API.

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

- **Stop Finder API**: Find transport stops by name or coordinates
- **Alerts API**: Get information about transport alerts and disruptions
- **Departure Monitor API**: Get real-time departure information for transport stops
- **MCP Implementation**: Structured as a Model Context Protocol service

## Usage Examples

MCP Examples coming soon. Standard Python examples below:

### Find Transport Stops

```python
from api import find_transport_stops

# Search by name
stops = find_transport_stops(stop_name="Central Station")

# Search by coordinates (Central Station area)
central_station = '151.206290:-33.884080:EPSG:4326'
stops = find_transport_stops(coord=central_station, radius=500)
```

### Get Transport Alerts

```python
from api import get_transport_alerts

# Get all current alerts
alerts = get_transport_alerts()

# Get alerts for a specific date
date_alerts = get_transport_alerts(date='22-03-2025')

# Get train alerts only (mot_type=1)
train_alerts = get_transport_alerts(mot_type=1)
```

### Monitor Real-time Departures

```python
from api import get_departure_monitor

# Get departures from Central Station
departures = get_departure_monitor("200060")  # Central Station ID

# Get departures for a specific time
from datetime import datetime
time_departures = get_departure_monitor("200060", time="15:30")

# Get only train departures
train_departures = get_departure_monitor("200060", mot_type=1)  # 1 = Train
```

## Demo Script

The project includes a comprehensive demo script that showcases all API functionality:

```bash
# Run the full demo
python demo.py

# Run specific sections
python demo.py --stops       # Stop finder demo
python demo.py --alerts      # Transport alerts demo
python demo.py --departures  # Departure monitoring demo
```

## Testing

### Local Testing

Run the complete test suite with pytest:

```bash
uv run pytest
```

Run with coverage reporting:

```bash
uv run pytest --cov=api
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

## License

This project is licensed under the [MIT License](LICENSE).
