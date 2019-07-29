def int(odd_sum(*args)):
    sum = 0
    for number in odd_sum():
        if number % 2:
            sum += number
    return sum


print(int(odd_sum(3,17,1,39,8,41,2,32,99,2)))
