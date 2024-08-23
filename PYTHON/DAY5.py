##a = 'today is'
##for i in a:
##    print('i=',i)
##
##
##for i in a:
##    print('i=',i,end=',')


##b = ['ayush','atul',12,45]
##for i in b:
##    print('i=',i,end=',')

##
##for i in a:
##    if i in 'AEIOUaeiou':
##        print(i)
##
##
##for i in a:
##    if i in 'AEIOUaeiou':
##        print(i,end='')



#input:todAy is thursday
#output:oAiua
##inpstr = input()
##for i in inpstr:
##    if i in 'AEIOUaeiou':
##        print(i,end='')





##inpstr = input()
##outstr = ''
##for i in inpstr:
##    if i in 'AEIOUaeiou':
##        outstr +=i
##print(outstr)



##def extractvowel(inpstr):
##    output = ''
##    for i in inpstr:
##        if i in 'AEIOUaeiou':
##            output += i
##    return output
##
##str = input()
##print(extractvowel(str))




##def extractnum(num):
##    output = ''
##    for i in num:
##        if i in '1234567890':
##            output += i
##    return output
##
##num = input()
##print(num,' = ',extractnum(num))



##def extractconsonant(inpstr):
##    output = ''
##    for i in inpstr:
##        if i in 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm':
##            output += i
##    return output
##
##str = input()
##print(extractconsonant(str))



##def extractvowel(inpstr):
##    total = 0
##    for i in inpstr:
##        if i in 'AEIOUaeiou':
##            total +=1
##    return total
##
##str = input()
##print("No of Vowels in :'",str,"'is",extractvowel(str))


##def extractnum(num):
##    total = 0
##    for i in num:
##        if i in '1234567890':
##            total +=1
##    return total
##
##num = input()
##print("No of digits in :'",num,"'is",extractnum(num))


def extract_spchar(inpstr):
    total = 0
    for i in inpstr:
        if i not in 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnmAEIOUaeiou0123456789':
            total +=1
    return total

str = input()
print("No of spchar in :'",str,"'is",extract_spchar(str))



