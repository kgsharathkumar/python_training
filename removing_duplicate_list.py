a=[1,2,8,8,9,2,3,4,4,5,6,1]
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)
list.sort(b)
print(b)
