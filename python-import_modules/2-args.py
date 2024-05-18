#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv)

    if num_args == 1:
        print("0 arguments.")
    elif num_args == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(num_args - 1))
        for i in range(1, num_args):
            print("{}: {}".format(i, sys.argv[i]))
