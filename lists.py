marks = [3, 5, 6, "Soham", True]
print(marks)
print(type(marks))

print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

# if 7 in marks:
#     print("Yes")

# else:
#     print("No")
print(marks[:])
print(marks[1:4:2])


list = [i*i for i in range(10)]
print(list)
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)

colors = ["voilet", "indigo", "green", "blue"]
rainbow = ["orange", "red", "brown"]
colors.sort()
print(colors)
l = [11, 45, 1, 2, 4, 6, 1]
l.reverse()
print(l)
newslist = colors.copy()
print(colors)
print(newslist)

colors.append("red")
print(colors)

colors.insert(1, "yellow")
print(colors)

colors.extend(rainbow)
print(colors)

l = colors + rainbow
print(l)