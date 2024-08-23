'''
WAP to print smallest digit from a number input
INPUT
456871
OUTPUT
1
'''

def smallest1(s):
    d = sorted(str(s))[0]
    return d
inp = int(input("Enter : "))
print(smallest1(inp))