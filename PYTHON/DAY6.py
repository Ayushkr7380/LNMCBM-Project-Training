###Binary2Decimal
##def binaryToDecimal(s):
##    return int(str(s),2)
##n = input('Enter binary number : ')
##print(binaryToDecimal(n))
##
##
###Binary2Octal
##def binarytToOctal(s):
##    return int(str(s),8)
##n = input('Enter binary number : ')
##print(binarytToOctal(n))
##
###Binary2Hexadecimal
##def binaryToHexadecimal(s):
##    return int(str(s),16)
##n = input('Enter binary number : ')
##print(binaryToHexadecimal(n))

###hexadecimalToDecimal
##def hexadecimalToDecimal(s):
##    return int(str(s),16)
##n = input('Enter hexadecimal number : ')
##print(hexadecimalToDecimal(n))


##def decimalToBinary(s):
##    return bin(int(s))
##n = input('Enter decimal number : ')
##print('Binary number is : ',decimalToBinary(n)[2:])
##
##def decimalToOctal(s):
##    return oct(int(s))
##n = input('Enter decimal number : ')
##print('Octal number is : ',decimalToOctal(n)[2:])
##
##
##def decimalToHexa(s):
##    return hex(int(s))
##n = input('Enter decimal number : ')
##print('Hexa number is : ',decimalToHexa(n)[2:])



##def binaryToHexadecimal(s):
##    return hex(s)
##n = int(input('Enter binary number : '))
##print('Hexadecimal : ',binaryToHexadecimal(n)[2:])


##def binaryToOctal(s):
##    return oct(s)
##n = int(input('Enter binary number : '),2)
##print('Octal : ',binaryToOctal(n)[2:])


#binary to octal/hexa # octal to binary/hexa # hexa to bin/oct


# print('{0},{1},{2}'.format('apple','banana','carrot'))

# print('{0} and {1} are good friends and {0} likes {2}'.format('ayush','aditya','maths'))

# a = 5
# b = 7
# c = a+b
# print('{0}+{1}={2}'.format(a,b,c))
# print('{0} + {1} = {2}'.format(a,b,c))
# print('{1}+{0}={2}'.format(a,b,c))


# def binaryToOctal(s):
#     return oct(s)[2:]
# n = int(input('Enter a binary number : '),2)
# print('Octal number is ',binaryToOctal(n))

# def binaryToHex(s):
#     return hex(s)[2:]
# n = int(input('Enter a binary number : '))
# print('Hex number is ',binaryToHex(n))

# def octalToBinary(s):
#     return bin(s)[2:]
# n = int(input('Enter a octal number : '),8)
# print('Binary number is ',octalToBinary(n))

def octalTohex(s):
    hex_num = hex(int(s, 8))[2:]
    return hex_num

octal_num = input('Enter an octal number: ')
print('Hexadecimal number is:', octalTohex(octal_num))








