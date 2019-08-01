N = int(input())
N_list = list(map(int,input().split()))

result = sorted(N_list)

print(result[0], result[-1])


