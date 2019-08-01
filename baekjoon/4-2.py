import sys

while True:
    line = sys.stdin.readline
    if not line:
        break
    else:
        A, B = map(int,line().split())
        print(A + B)