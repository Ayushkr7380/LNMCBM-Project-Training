#Reverse vowels in a given string
#hello
#eo#oe
#Holle
def a(s):
    #Extracting vowel from the string
    v=''
    for i in s:
        if i in 'AEIOUaeiou':
            v = v + i

    #Reversing the string
    reversed_vowel = v[::-1]
    # print(reversed_vowel)

    #Replacing the actual vowel of the string to the reversed vowel 
    
    out = ''
    n = 0
    for i in s:
        if i in "aeiouAEIOU":
            out += reversed_vowel[n]
            n+=1
        else:
            out+=i
    return out
inp = input("Enter anything : ")
print(a(inp))
            

    