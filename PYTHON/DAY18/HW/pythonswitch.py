# def p_rectangle():
#     length1 = float(input("Enter the length of rectangle : "))
#     breadth1 = float(input("Enter the breadth of rectangle : "))

#     perimeter1 = 2 * (length1 + breadth1)

#     print(f'Perimeter of rectangle is {perimeter1}')
# def a_rectangle():
#     length1 = float(input("Enter the length of rectangle : "))
#     breadth1 = float(input("Enter the breadth of rectangle : "))

#     area1 =length1 * breadth1

#     print(f'Area of rectangle is {area1}')
# def p_square():
#     side1 = float(input("Enter the side of square : "))

#     perimeter2 =4 * side1

#     print(f'Perimeter of square is {perimeter2}')
# def a_square():
#     side2 = float(input("Enter the side of square : "))

#     area2 =side2 * side2

#     print(f'Area of square is {area2}')
# def c_circle():
#     rad1 = float(input("Enter the radius of circle : "))

#     circum1 = 2 * 3.14 * rad1

#     print(f'Circumference of a circle  is {circum1}')
# def a_circle():
#     rad2 = float(input("Enter the radius of circle : "))

#     area3 = 3.14 * rad2 * rad2

#     print(f'Area of a circle  is {area3}')
# def choose():
#     print("Press 1 for Perimeter of rectangle ")
#     print("Press 2 for Area of rectangle ")
#     print("Press 3 for Perimeter of Square ")
#     print("Press 4 for Area of Square ")
#     print("Press 5 for Circumference of circle ")
#     print("Press 6 for Area of circle ")
#     print("Press 0 for Quit")

# dict1 = {
#     1:p_rectangle,
#     2:a_rectangle,
#     3:p_square,
#     4:a_square,
#     5:c_circle,
#     6:a_circle
# }
# select = 1
# while True:
#     if select == 0:
#         break
#     choose()
#     select = int(input("Choose any of these Options : "))
#     if(select > 0 and select <=6):
#         dict1[select]()
    


    
def string():
    print("String")

def float_(v):  
    print("Float",v)

def list_(value):  
    print("List:", value)

def tuple_():
    print("Tuple")

def dict_():
    print("Dictionary")

def set_():
    print("Set")

def bol():
    print("Boolean")

def comp():
    print("Complex number")

def chose():
    a = input("Enter a data value:")
    if a.isdigit():
        Integer(int(a))
    elif a.lower() in ['true', 'false']:  
        bol()
    elif '.' in a:  
        float_(float(a))
    elif a.startswith('[') and a.endswith(']'):  
        list_(eval(a))
    elif a.startswith('(') and a.endswith(')'):  
        tuple_()
    elif a.startswith('{') and a.endswith('}'):  
        if ':' in a:
            dict_()
        else:
            set_()
    elif 'j' in a:  # Check for complex number (contains 'j' as imaginary part)
        comp()
    else:
        string()  # Default case: if none of the above conditions met, treat as string

def Integer(value):
    print("Integer:", value)

chose()
