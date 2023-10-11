#!/usr/bin/python3
import sys
import signal


def signal_handler(sig, frame):
    """Handle keyboard interruption and print statistics."""
    print_statistics()
    sys.exit(0)


def print_statistics():
    """Print the statistics for the log."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    total_size = 0
    line_count = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) > 1:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_statistics()

    except KeyboardInterrupt:
        print_statistics()
        sys.exit(0)
