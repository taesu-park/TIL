def palindrome(word):
    for i in range(0,len(word)//2):
        if word[i]!=word[-i-1]:
            return False
    return True
print(palindrome('토마토'))