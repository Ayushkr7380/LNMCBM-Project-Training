def pal(s):
    s = str(s)
    temp = s[::-1]
    if s == temp:
        return 'palindrome'
    else:
        return 'Not palindrome'
inp = input('Enter anything')
print(pal(inp))