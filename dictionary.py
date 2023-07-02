dic = {
    "Soham" : "Human Being",
    "Spoon" : "Object"
}

print(dic["Soham"])

info = {'name':"Soham", 'age':17, 'eligible': True}
print(info)
print(info['name'])
print(info.get('name'))

# print(info['name2'])
print(info.get('name2'))

print(info.keys ())


print(info.items())
for key, values in info.items():
    print(f"The value corresponding to the key {key} is {values}")