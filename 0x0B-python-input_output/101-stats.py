#!/usr/bin/python3
import sys


def print_stats(status_codes, total_size):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    status_codes = {}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            tokens = line.split()
            if len(tokens) > 1:
                status_code = tokens[-2]
                file_size = int(tokens[-1])
                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

            if line_count % 10 == 0:
                print_stats(status_codes, total_size)

    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise

    print_stats(status_codes, total_size)
