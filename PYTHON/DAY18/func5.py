def sun():
    print('Sunday')
def mon():
    print('Monday')
def tue():
    print('Tuesday')
def wed():
    print('Wednesday')
def thus():
    print('Thrusday')
def fri():
    print('Friday')
def sat():
    print('Saturday')
def choice():
    # print("1:Sunday")
    # print("2:Monday")
    # print("3:Tuesday")
    # print("4:Wednesday")
    # print("5:Thrusday")
    # print("6:Friday")
    # print("7:Saturday")
    print("0:Quit")
select = {
    1:sun,
    2:mon,
    3:tue,
    4:wed,
    5:thus,
    6:fri,
    7:sat
}
selection = 1
while True:
    if selection == 0:
        break
    choice()
    selection = int(input('Select any given option:'))
    if(selection>0) and (selection<8):
        select[selection]()
