#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics."""

import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        total_size += int(data[-1])
        status_code = data[-2]
        if status_code in status_codes:
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print("{}: {}".format(code, count))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))
