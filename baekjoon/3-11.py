N, X = map(int,input().split())
numbers = list(map(int,input().split()))
A = []

for number in numbers:
    if number < X:
        A.append(str(number))
print(' '.join(A)) # -> join은 str을 변수로 받아야함.