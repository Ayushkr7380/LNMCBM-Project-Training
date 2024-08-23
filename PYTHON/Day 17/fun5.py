print("Using Normal function")
inpL = ['anjali','divya','pritam','wasim','gaurav']
def rev_str(a):
    return a[::-1]
outL = list(map(rev_str,inpL))
print(inpL)
print(outL)

#outL = ['ilajna', 'ayvid', 'matirp', 'misaw', 'varuag']

print("Using Lambda function")
inpL1 = ['anjali','divya','pritam','wasim','gaurav']

outL1 = list(map(lambda x : x[::-1],inpL1))
print(inpL1)
print(outL1)

fruits = ["apple","mango","banana"]
filterfruits = list(filter(lambda x : len(x)==5,fruits))
print(filterfruits)
