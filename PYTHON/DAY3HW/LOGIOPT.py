#<-----------------Logical operator-------------------->

#and and or operator
def and_or():
    x = 10
    return x
a = and_or()
print('Is this statement true?:',a>3 and a<5) #Is this statement true?: False
print('Any one statement is true?:',a>3 or a<5) #Any one statement is true?: True
print('Each statement is true :',(a>3 and a<5)) #Each statement is true : False
print('Each statement is true then return False and vise-versa:',(not(a>3 and a<5))) #Each statement is true then return False and vise-versa: True


