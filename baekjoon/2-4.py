H , M = map(int,input().split())

M = M - 45



if H >0 and M < 0:
    M = M + 60
    H = H - 1
    print(H, M)

elif H <= 0 and M < 0:
    H = H + 23
    M = M + 60
    print(H, M)
    
else:
    print(H, M)

