'''
Script to extract signatures from lib/Image/ExifTool/JPEGDigest.pm of exiftool
'''

import re
import sys
from pprint import pprint

# Define the pattern to match
pattern = re.compile(r"'([a-f0-9]{32})(?::(\d+))?'\s*=>\s*'([^']+)'")

# Initialize an empty dictionary
data = {}

# Process each line from standard input
for line in sys.stdin:
    # Try to find a match in the line
    match = pattern.search(line)

    # If a match was found
    if match:
        # Extract the fields from the match
        hash = match.group(1)
        subsampling = match.group(2) or ''
        description = match.group(3)

        # Add the data to the dictionary
        data[hash] = {'subsampling': subsampling, 'description': description}

# Pretty print the dictionary
pprint(data)

