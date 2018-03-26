list1 = [1,2,3,5,7,13,27,39,99,106]
list2 = [4,5,7,23,24,27,40,44,79,106,125]
list3 = []

for x in list2:
    if x in list1:
        list3.append(x)

print(list1,"ve",list2,"listelerindeki ortak sayılar: \n\n", list3)
