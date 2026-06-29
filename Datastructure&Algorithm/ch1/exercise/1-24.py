def count_vowel(str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in range(0, len(str)):
        if(str[i] in vowel):
            cnt += 1
    return cnt

str1 = "aeiou"
print(count_vowel(str1))