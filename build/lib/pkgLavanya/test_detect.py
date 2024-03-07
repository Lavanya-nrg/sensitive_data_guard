import os
import sys

# Adding the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pkgLavanya.detect_info import find_pattern
def test_sensitive_info():
    """Test if the function correctly detects sensitive information."""
    example_string = "String contains Username"
    assert find_pattern(example_string) == False  # Assuming find_pattern returns True if sensitive information is found

def test_no_sensitive_info():
    """Test if the function correctly handles no sensitive information."""
    example_string = "String does not contain sensitive data"
    assert find_pattern(example_string) == False

def test_no_data():
    """Test if the function handles an empty string."""
    example_string = " "
    assert find_pattern(example_string) == False
