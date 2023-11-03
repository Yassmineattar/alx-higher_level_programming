#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    res = 0
    for i in sys.argv:
        res += int(i)
        print("{}".format(res))
