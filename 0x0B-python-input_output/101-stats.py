#!/usr/bin/python3
"""This module is for parsing logs from stdin and computing metrics."""

import sys
import signal


def print_stats(status_codes, total_size):
    """Prints the statistics of status codes and total file size."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """Handles the keyboard interruption and prints statistics."""
    print_stats(status_codes, total_size)
    sys.exit(0)


if __name__ == "__main__":
    """Main function that reads stdin line by line and computes metrics."""
    total_size = 0
    line_count = 0
    status_codes = {}

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        try:
            parts = line.strip().split(" ")
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(status_codes, total_size)

        except Exception as e:
            continue
