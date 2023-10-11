#!/usr/bin/python3
"""This module processes log data from stdin and calculates metrics.

It prints out the total file size and the count of status codes
after every 10 lines or upon receiving a keyboard interruption (CTRL + C).
"""

import sys
import signal


def display_metrics(total_size, code_count):
    """Displays the metrics for file size and status codes.

    Args:
        total_size (int): Accumulated file size.
        code_count (dict): Accumulated count of status codes.
    """
    print(f"File size: {total_size}")
    for code in sorted(code_count.keys()):
        print(f"{code}: {code_count[code]}")


def handle_interrupt(signum, frame):
    """Handles keyboard interrupt and displays metrics."""
    display_metrics(total_size, code_count)
    sys.exit(0)


if __name__ == "__main__":
    total_size = 0
    code_count = {}
    line_counter = 0
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    signal.signal(signal.SIGINT, handle_interrupt)

    for entry in sys.stdin:
        line_counter += 1

        elements = entry.strip().split()
        try:
            total_size += int(elements[-1])
        except (IndexError, ValueError):
            continue

        status = elements[-2] if len(elements) > 1 else None
        if status in valid_codes:
            code_count[status] = code_count.get(status, 0) + 1

        if line_counter % 10 == 0:
            display_metrics(total_size, code_count)
