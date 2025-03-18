import pytest
import sys
import os

# Add parent directory to path to ensure imports work correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import from the consolidated test file
from test_api import TestCoordinateAPI

# This file is kept for backward compatibility
# All tests have been moved to test_api.py

if __name__ == "__main__":
    print("Note: Tests have been consolidated into test_api.py")
    pytest.main(["-v", "test_api.py::TestCoordinateAPI"])
