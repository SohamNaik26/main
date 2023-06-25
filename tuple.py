tup = (1, 2, 76, 342, 199, True, "green")
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[5])

if 3421 in tup:
    print("Yes 342 is present inn tuple")
tup2 = tup[2: 4]
print(tup2)

countries = ("Spain", "Italy", "Scotland", "Germany")
temp = list(countries)
temp.append("Russia")    #to add items at the end
temp.pop(3)    # To remove items
temp[2] = "Finland"
countries = tuple(temp)
print(countries)



tuple1 = (0, 1, 2, 3, 4, 3, 5, 3, 3)
res = tuple1.count(3)
print('Count of 3 in tuple1 is:', res)

res2 = len(tuple1)
print("Count of 3 in tuple 1 is:", res2)

res1 = tuple1.index(2)
print("first occurence of 2 in res1 is:", res1)