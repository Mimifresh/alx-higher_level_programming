#!/usr/bin/pyhon3
def safe_print_integer(value):
    try:
        int(value)
        print(value)

        return True

    except (TypeError, ValueError):

        return False    
