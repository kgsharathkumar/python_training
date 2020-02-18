list1 = [1, 2, 3, 1, 2, 5, 6, 7, 8]
list2 = [1,2,9,6,4]
list3 = []
for x in list2:
    if x not in list3:
        list3.append(x)
    for x in list1: 
        if x not in list3:
            list3.append(x)         
print(list3)
list.sort(list3)
print(list3)
    
