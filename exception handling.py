a = input("Enter the number: ")
print("multiplication table of {a} is:")

for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")

print("Some imp lines of code")
print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])

except ValueError:
    print("Number entered is not a integer")

except IndexError:
    print("Index Error")
