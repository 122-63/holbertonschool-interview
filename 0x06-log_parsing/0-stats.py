#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
"""
from sys import stdin


status_code = {"200":0, "301":0, "400":0, "401":0,
               "403":0, "404":0, "405":0, "500":0}
sum = 0


def print_status():
    """Print status"""
    print("File size: {}".format(sum))
    for key, val in sorted(status_code.items()):
        if val > 0:
            print("{}: {}".format(key, val))


if __name__ == "__main__":
    try:
        for i, line in enumerate(stdin, 1):
            try:
                info = line.split()
                sum += int(info[-1])
                if info[-2] in status_code.keys():
                    status_code[info[-2]] += 1
            except:
                pass
            if not i % 10:
                print_status()
    except KeyboardInterrupt:
        print_status()
        raise
    else:
        print_status()
