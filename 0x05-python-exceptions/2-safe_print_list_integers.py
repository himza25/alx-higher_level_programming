#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints first 'x' integers in a list.
    
    Args:
        my_list: list of elements
        x: number of elements to print from list

    Returns:
        The actual number of integers printed
    """
    num_printed = 0 
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_printed += 1
        except IndexError:
            raise
        except (ValueError, TypeError):
            pass
    print("")
    return num_printed
