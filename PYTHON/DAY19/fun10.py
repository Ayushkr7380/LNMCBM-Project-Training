def remove_duplicate(s):
    non = ''
    for i in s:
        if i not in non:
            non += i
    return non
inp1 = input("Enter anything : ")
a = remove_duplicate(inp1)
print(f"First Non Repititive character is {a}")

#ayush abhi

