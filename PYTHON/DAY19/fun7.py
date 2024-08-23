def extract_vowel(s):
    vowel1 = ''
    for i in s:
        if i in 'AEIOUaeiou':
            vowel1+=i
    return vowel1
str1 = input("Enter anything : ")
a = extract_vowel(str1)
print(f'Vowel in : {str1} is {a}')