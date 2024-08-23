def extract_digits(s):
    digit1 = ''
    for i in s:
        if i in '1234567890':
            digit1+=i
    return digit1
str1 = input("Enter anything : ")
a = extract_digits(str1)
print(f'Digits in : {str1} is {a}')