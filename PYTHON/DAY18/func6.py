E = {0,2,4,6,8}
N = {1,2,3,4,5}

#set union
print("Union of E and N is ",E|N)

#setintersection
print("Intersection of E and N is",E&N)

#set difference
print("Difference of E and N is",E - N)
print("Difference of N and E is",N - E)

#set symmetric difference
print("symmetric difference of E and N is ",E ^ N)
print("symmetric difference of E and N is ",(E - N ) | (N - E))