#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Trying to format the value as an integer and print it
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        # Catching ValueError if the value can't be converted to an integer
        return False
