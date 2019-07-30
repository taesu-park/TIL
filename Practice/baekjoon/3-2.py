T = int(input())

for i in range(1, T+1):

    A, B = list(map(int,input().split()))


for x, y in zip(A, B):
    print(x,y)
