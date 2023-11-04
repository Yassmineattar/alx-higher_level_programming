#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    L = len(sys.argv)
    if L == 1:
        print("{} arguments.".format(L - 1))
    elif L == 2:
        print("{} argument:".format(L - 1))
    else:
        print("{} arguments:".format(L - 1))
    for i in range(1, L):
        print("{}: {}".format(i, sys.argv[i]))
