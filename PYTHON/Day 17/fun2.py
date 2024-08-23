def printinfo( arg1 , *vt):
    '''This function accepts varaible length argument.'''

    print("arg1:",arg1)
    print("Contents of variable length tuple is : ")
    for i in vt:
        print(i,end=',')
    print()
    return
printinfo('Ayush')
printinfo('Ayush','Adarsh','Aditya','Sonu')