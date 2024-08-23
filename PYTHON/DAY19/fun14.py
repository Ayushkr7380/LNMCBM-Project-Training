def non_repititive_character(s):
    count_character = ''
    #Count the number of times the character is repeated..
    for i in s:
        count_character += i * s.count(i)
    #Find the first character with count 1
    for j in count_character:
        if count_character.count(j) == 1:
            return j
    return None
inp = input('Enter anything : ')
print(non_repititive_character(inp))