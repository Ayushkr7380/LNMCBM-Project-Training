#Extract first digit (n) from input string and return character at nth position
#input
#today is 3rd day
#output
#d

def ext1(s):
    digit = ''
    for i in s:
        if i in '0123456789':
            digit+=i
    return int(digit[0])
inp = input('Enter')
print(inp[ext1(inp) - 1])