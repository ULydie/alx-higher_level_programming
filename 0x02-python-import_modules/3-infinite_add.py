#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    sum = 0
    for c in range(1,n):
        sum += int(sys.argv[c])
    print(sum)
