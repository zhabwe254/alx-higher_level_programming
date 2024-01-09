#!/usr/bin/python3
import sys
import signal

def print_stats(total_size, status_codes):
    """Prints the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Handles keyboard interrupt"""
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def parse_line(line):
    """Parses a log line and returns (status_code, file_size)"""
    parts = line.split()
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        status_code, file_size = parse_line(line)
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    sys.exit(0)
