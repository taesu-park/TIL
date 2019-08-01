M = N = int(input())

if len(str(N)) == 1:
    N * 10

A = N // 10
B = N % 10
C = A + B
N = B*10 + C % 10
count = 1
while M != N:
    if len(str(N)) == 1:
        N * 10
    A = N // 10
    B = N % 10
    C = A + B
    N = B*10 + C % 10
    count += 1

print(count)