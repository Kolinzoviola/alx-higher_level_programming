#!/usr/bin/python3

if __name__ == "__main__":      # main script program
    """Print the number of and list of arguments."""        # docstring
    import sys      # imports python modules

    count = len(sys.argv) - 1       # counts commandline arguments
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):      # loop iterates over the command-line arguments
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
