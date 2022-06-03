#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
"""
import sys


status_code = {"200":0, "301":0, "400":0, "401":0,
               "403":0, "404":0, "405":0, "500":0}
sum = 0


def print_status():
    """Print status"""
    global sum

    print("File size: {}".format(sum))
    sort = sorted(status_code.keys())
    for i in sort:
        if status_code[i] > 0:
            print("{}: {}".format(i, status_code[i]))


if __name__ == "__main__":
    count = 0 
    try: 
        for data in sys.stdin:
            try:
                fact = data.split(' ')
                """ If there is a status code """
                if fact[-2] in status_code:
                    status_code[fact[-2]] += 1
                """ If there is a lenght """
                sum += int(fact[-1])
            except:
                pass
            """ Printing control """
            count += 1
            if count == 10:
                print_status()
                count = 0
    except KeyboardInterrupt:
        print_status()
        raise
    else:
        print_status()


