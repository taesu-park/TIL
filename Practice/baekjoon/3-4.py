import sys

input = sys.stdin.readline

T = int(input().rstrip())


for i in range(1, T+1):
    A, B = map(int,input().rstrip().split())
    print(A + B)