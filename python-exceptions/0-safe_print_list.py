#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # initializes variable count to 0
    count = 0

    try:  # try-except block then loop over elements
        for element in my_list[:x]:
            print(element, end='')
            count += 1
    except IndexError:
        pass
    print()  # print newline character
    return count
