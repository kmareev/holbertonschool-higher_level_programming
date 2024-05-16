#!/usr/bin/python3

import sys

if __name__ == "__main__":
    total = 0

    if len(sys.argv) == 1:
        print("No arguments passed")
    else:
        for i in range(1, len(sys.argv)):
            total += int(sys.argv[i])
        print(total)
