print("**  Calculator  **")
print("\n")

num1 = float(input("Enter the first number here: "))
num2 = float(input("Enter the second number here: "))

print(
    "Enter 1 for 'Addition' \nEnter 2 for 'Subtraction' \nEnter 3 for 'Multiply' \nEnter 4 for 'Division'"
)

Entered_number = int(input("choice a number from 1 to 4: "))

if Entered_number == 1:
    print("Addition of num1 and num2 is : ", num1 + num2)

elif Entered_number == 2:
    print("Subraction of num1 and num2 is : ", num1 - num2)

elif Entered_number == 3:
    print("Multiplication of num1 and num2 is : ", num1 * num2)

else:
    print("Division of num1 and num2 is : ", num1/num2)