def palin(word):
    # word 단어를 처음값 - 끝값 => len(word) // 2
    for i in range(0,len(word)//2):
        if word[i]==word[-i-1]:
            continue
        # 다르면, 팰린드롬이 아니니까 False 리턴하고 더이상 확인하지 않는다.
        else:
            return False
    # 다 끝나면, 팰린드롬이 맞으니까 True 리턴
    return True


print(palin('토마토토마토'))

def palin(word):
    # word 단어를 처음값 - 끝값 => len(word) // 2
    for i in range(len(word)//2):
        if word[i]!=word[-i-1]:
            return False
    # 다 끝나면, 팰린드롬이 맞으니까 True 리턴
    return True



def palin(word):
    return word == word[::-1]
print(palin('토마토마토'))