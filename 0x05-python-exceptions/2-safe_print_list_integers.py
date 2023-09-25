#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints and counts the first x integers in a list.
    
    Args:
        my_list: List to print from.
        x: Number of elements to attempt to print.
        
    Returns:
        Number of integers printed.
    """
    counter = 0  # Initialize counter for the number of integers printed
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            counter += 1  # Increment counter if successfully printed an integer
        except IndexError:
            pass  # Handle if index is out of range
        except (ValueError, TypeError):
            pass  # Skip the iteration if the value is not an integer
    print("")
    return counter
