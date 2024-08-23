#n1=int(input('Enter a Number :'),10)
#n2=int(input('Enter another Number : '),10)
#sum = n1 + n2
#print(str(n1)+'+'+str(n2)+'='+str(n1+n2))
#print('aman','ayush',sep='#@')
#print(n1,'+',n2,'=',sum,sep='')
#print(n1,'-',n2,'=',n1-n2,sep='')
#print(n1,'*',n2,'=',n1*n2,sep='')
#print(n1,'/',n2,'=',n1/n2,sep='')

##def add():
##    n1 = int(input('Enter 1st Number : '))
##    n2 = int(input('Enter 2nd Number : '))
##    print(n1,'+',n2,'=',n1+n2,sep='')
##    return None
##def sub():
##    n1 = int(input('Enter 1st Number : '))
##    n2 = int(input('Enter 2nd Number : '))
##    print(n1,'-',n2,'=',n1-n2,sep='')
##    return
##
##def mul():
##    n1 = int(input('Enter 1st Number : '))
##    n2 = int(input('Enter 2nd Number : '))
##    print(n1,'*',n2,'=',n1*n2,sep='')
##    
##def div():
##    n1 = int(input('Enter 1st Number : '))
##    n2 = int(input('Enter 2nd Number : '))
##    print(n1,'/',n2,'=',n1/n2,sep='')
##    return None
##add()
##sub()
##mul()
##div()


##def add1(n1,n2):
##    res= n1+n2
##    return res
##num1 = int(input('Enter 1st Number : '),10)
##num2 = int(input('Enter 2nd Number : '),10)
##print(num1,'+',num2,'=',add1(num1,num2),sep='')
##
##def sub1(n1,n2):
##    res= n1-n2
##    return res
##num1 = int(input('Enter 1st Number : '),10)
##num2 = int(input('Enter 2nd Number : '),10)
##print(num1,'-',num2,'=',sub1(num1,num2),sep='')
##
##def mul1(n1,n2):
##    res= n1*n2
##    return res
##num1 = int(input('Enter 1st Number : '),10)
##num2 = int(input('Enter 2nd Number : '),10)
##print(num1,'*',num2,'=',mul1(num1,num2),sep='')
##
##def div1(n1,n2):
##    res= n1/n2
##    return res
##num1 = int(input('Enter 1st Number : '),10)
##num2 = int(input('Enter 2nd Number : '),10)
##print(num1,'/',num2,'=',div1(num1,num2),sep='')


def add(num1,num2):
    res= num1+num2
    temp =''+str(num1)+'+'+str(num2)+'='+str(res)
    return temp
n1 = int(input('Enter 1st Number : '))
n2 = int(input('Enter 2nd Number : '))
print(add(n1,n2))

def sub(num1,num2):
    res= num1-num2
    temp =''+str(num1)+'-'+str(num2)+'='+str(res)
    return temp
n1 = int(input('Enter 1st Number : '))
n2 = int(input('Enter 2nd Number : '))
print(sub(n1,n2))

def mul(num1,num2):
    res= num1*num2
    temp =''+str(num1)+'*'+str(num2)+'='+str(res)
    return temp
n1 = int(input('Enter 1st Number : '))
n2 = int(input('Enter 2nd Number : '))
print(mul(n1,n2))

def div(num1,num2):
    res= num1/num2
    temp =''+str(num1)+'/'+str(num2)+'='+str(res)
    return temp
n1 = int(input('Enter 1st Number : '))
n2 = int(input('Enter 2nd Number : '))
print(div(n1,n2))

    
