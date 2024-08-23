def count_vowel(s):
    vowel = 0 
    s = str(s)
    for i in s:
        if i in 'AEIOUaeiou':
            vowel = vowel + 1
    return vowel
str1 = input('Enter any string : ')
a = count_vowel(str1)
print(f'No. of vowel in {str1} is {a}')