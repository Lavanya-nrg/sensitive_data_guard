import os
import re
from .config import patterns

# Path to the file containing data to be checked
#file_path = "/home/user1/Desktop/sensitive_data_guard/sensitive_data_gaurd/data.txt"


# Specify the directory and file name
directory = '/home/user1/Desktop/pkgLavanya/pkgLavanya'
filename = 'data.txt'

# Combine the directory and filename to create a file path
file_path = os.path.join(directory, filename)

# Print the generated file path
print("Generated File Path:", file_path)

def find_pattern(input_string):
    """
    Check if any pattern from the list 'patterns' is matched in the input string.

    Args:
        input_string (str): The input string to be checked for patterns.

    Returns:
        bool: True if any pattern is matched, False otherwise.
    """
    matched = False
    for line in input_string.split("\n"):
        # Iterate through each pattern to check for a match
        for pattern in patterns:
            if re.match(pattern, line):
                matched = True
                break
        if not matched:
            matched = False  # Reset the flag for the next line
    return matched

# Open the file and read its content
with open(file_path) as file:
    content = file.read()

# Print the result of pattern matching
print(find_pattern(content))
