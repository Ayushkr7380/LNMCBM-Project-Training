def count_spchar(s):
    spchar = 0
    temp = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    for i in s:
        if i not in temp:
            spchar+=1
    return spchar
str1 = input("Enter anything : ")
a = count_spchar(str1)
print(f'No. of special character in {str1} is {a}')