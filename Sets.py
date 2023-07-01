s = {2, 4, 6, 2, 8}
print(s)

info = {"Soham", 26, 7, False, 6.7}
print(info)

Soham = set()
print(type(Soham))

for value in info:
    print(value)


cities = {"Tokyo", "Beijing", "Berlin", "New York", "Madrid"}
cities2 = {"Tokyo", "Madrid","Delhi", "Mumbai"}
cities3 = cities.union(cities2)
print(cities3)

cities.intersection_update(cities2)
print(cities)

cities4 = cities.intersection(cities2)
print(cities4)

cities5 = cities.symmetric_difference(cities)
print(cities5)

cities6 = cities.isdisjoint(cities2)
print(cities6)

cities7 = {"Tokyo", "Beijing", "Madrid"}
print(cities.issuperset(cities7))
print(cities7.issubset(cities))

cities.clear()
print(cities)

s1 = {1, 3, 5, 6}
s2 = {2, 4, 8}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

