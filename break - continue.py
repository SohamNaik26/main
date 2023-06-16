for i in range(12):
    print("5 X", i, "=", 5 * i)
    if(i == 10):
        break

print("Loop ko chhodkar nikal gaya")


for i in range(12):
    print("3 X", i, "=", 3 * i)
    if(i == 10):
        continue
print("Loop ko chhodkar nikal gaya")


i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break