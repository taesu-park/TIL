N = int(input())
a = [i for i in range(1, N+1)]
for x in reversed(a): # -> sorted(), reversed()는 return O 
    print(x)
