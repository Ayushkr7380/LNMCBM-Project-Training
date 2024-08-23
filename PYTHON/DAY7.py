##def checkPalindrome(s):
##    s = str(s)
##    temp = s[::-1]
##    if temp == s:
##        return 'Palindrome'
##    else:
##        return 'Not Palindrome'
##    return None
##str1 = input()
##a = checkPalindrome(str1)
##print(a)


#Check if the string is anagram or not

##def checkAnagram(s1,s2):
##    if sorted(s1) == sorted(s2):
##        return 'Anagram'
##    else:
##        return 'Not Anagram'
##    
##inp = input().split()
##print(checkAnagram(inp[0],inp[1]))


#print first non-repetitive character of string
##
##def printNonRepitiveChar(s):
##    for i in s:
##        if s.count(i) == 1:
##            return i
##inp = input()
##print(printNonRepitiveChar(inp))


#remove/delete vowels from a string
##def removeVowels(s):
##    temp  =''
##    for i in s:
##        if i not in 'AEIOUaeiou':
##            temp = temp + i
##    return temp
##str1 = input()
##a  = removeVowels(str1)
##print('String',str1,'without vowel is',a)


#remove/delete digits from a string
##def removeDigits(s):
##    temp  =''
##    for i in s:
##        if i not in '0123456789':
##            temp = temp + i
##    return temp
##str1 = input()
##a  = removeDigits
##(str1)
##print('String',str1,'without digits is',a)



#remove duplicate characters from a string
##def remove_duplicate(str1):
##    str2=''
##    for i in str1:
##        if i not in str2:
##            str2+=i
##    return str2
##str1 = input()
##a = remove_duplicate(str1)
##print('String',str1,'without duplicate string is',a)


#extract even digits

##def extractEvenDigits1(d):
##    s = str(d)
##    temp = ''
##    for i in s:
##        if i in '02468':
##            temp +=i
##    return int(temp)
##a = int(input())
##print(extractEvenDigits1(a))

##def extractEvenDigits2(d):
##    s = str(d)
##    temp = ''
##    for i in s:
##        if int(i)%2 == 0 :
##            temp +=str(i)
##    return int(temp)
##a = int(input())
##print(extractEvenDigits2(a))

#extract odd digits

##def extractOddDigits1(d):
##    s = str(d)
##    temp = ''
##    for i in s:
##        if i  in '13579':
##            temp +=i
##    return int(temp)
##a = int(input())
##print(extractOddDigits1(a))

##def extractOddDigits2(d):
##    s = str(d)
##    temp = ''
##    for i in s:
##        if int(i)%2 != 0:
##            temp +=str(i)
##    return int(temp)
##a = int(input())
##print(extractOddDigits2(a))


#remove even digits

##def removeEvenDigits1(s):
##    temp = ''
##    for i in s:
##        if i not in '02468':
##            temp +=i
##    return temp
##a = input()
##print(removeEvenDigits1(a))

#remove odd digits

##def removeOddDigits1(s):
##    temp = ''
##    for i in s:
##        if i not in '13579':
##            temp +=i
##    return temp
##a = input()
##print(removeOddDigits1(a))


##def extractdigit(s):
##    temp = ''
##    for i in s:
##        if i in '0123456789':
##            temp+=i
##    return int(temp[0])
##a = input()
##print(a[extractdigit(a) - 1])
##n = extractdigit(a)
##print(a[n-1])

##def extractdigit(s):
##    temp = ''
##    for i in s:
##        if i in '0123456789':
##            temp+=i
##    if temp[1]:
##        return int(temp[1])
##    return int(temp[0])
##a = input()
##print(a[extractdigit(a) - 1])

##print(ord('0'))
##print(ord('1'))
##
##a  = '123112'
##print(sorted(a))
##print(sorted(a)[0])
##
##
##
##
##


def smallestdigit(d):
    s = str(d)
    temp = ''
    for i in s:
        if i in '0123456789':
            temp+=i
    sort1 = sorted(temp)
    return sort1[0]
a = int(input())
print(smallestdigit(a))
