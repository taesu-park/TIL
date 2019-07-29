A = int(input())

if not A % 4 and A % 100:
    print('1')
elif not A % 400:
    print('1')
else:
    print('0')