#!/usr/bin/python3

"""
Script reads stdin line by line and computes metrics.
"""

import sys


line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        # TODO
        # Handle the logic to compute other metrics based on the line content

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("\nProcess was interrupted by user")

print(f"Total lines read: {line_count}")
# TODO
# Handle the logic to print other computed metrics
