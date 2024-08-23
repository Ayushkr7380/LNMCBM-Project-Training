import operator
d = {'first':[100,60,90],
     'second':[20,10,80],
     'third':[11,44,22],
     'five':[50,30,70]
     }

print('Original Dictionary:\n',d)
sorted_d = sorted(d.values(),key=operator.itemgetter(1),reverse=False)
print('Dictionary in accending order by value:\n',sorted_d)
sorted_d = sorted(d.values(),key=operator.itemgetter(1),reverse=True)
print('Dictionary in decending order by value :\n',sorted_d)