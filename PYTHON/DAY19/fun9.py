def extract_even(d):
    even1 = ''
    s = str(d)
    for i in s:
        if i in '02468':
            even1+=i
    return int(even1)
    #     i1 = int(i)
    #     if i1%2==0:
    #         even1+=str(i1)
    # return even1
digits1 = int(input("Enter any number : "))
a = extract_even(digits1)
print(f"Even digits in {digits1} is {a}")
