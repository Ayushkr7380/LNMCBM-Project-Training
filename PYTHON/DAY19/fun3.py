def count_consonant(s):
    consonant = 0 
    s = str(s)
    for i in s:
        if i in 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm':
            consonant = consonant + 1
    return consonant
str1 = input('Enter any string : ')
a = count_consonant(str1)
print(f'No. of consonants in {str1} is {a}')