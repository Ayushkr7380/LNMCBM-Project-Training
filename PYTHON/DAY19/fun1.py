#Check if the String is Anagram or not

def checkanagram(s1,s2):
    if sorted(s1) == sorted(s2):
        return 'anagram'
    else:
        return 'Not anagram'
inp = input().split()
print(checkanagram(inp[0],inp[1]))