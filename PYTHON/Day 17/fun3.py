def add(*s):
    sum = 0
    for i in s:
        sum = sum + i
    print(f'Sum of {s} is {sum}')
add(1)
add(1,2)
add(1,2,3)
add(1,2,3,4)