def extract_consonant(s):
    consonant1 = ''
    for i in s:
        if i in 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm':
            consonant1+=i
    return consonant1
str1 = input("Enter anything : ")
a = extract_consonant(str1)
print(f'Consonant in : {str1} is {a}')