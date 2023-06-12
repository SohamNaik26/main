a = int(input("Enter your age"))
print("Your age is:", a)

# print(a > 18)
# print(a < 18)
# print(a >= 18)
# print(a <= 18)
# print(a == 18)
# print(a != 18)
if(a >= 18):
    print("You can drive")
    print("Yes")
else:    
    print("You cannot drive")
    print("No")

applePrice = 20
budget = 200

if (applePrice <= budget):
    print("Alexa add apples to the cart.")

elif (budget - apple >= 70):
    print("Add 1 kg apple to cart.")    

else:
    print("Alexa don't add apples to the cart.")    
    
#  3rd question   

num = 18
if (num < 0):
    print("Number is negative.")
elif(num > 0):
    if(num > 10 and num <= 20):
        print("Number is between 11 - 20")
    else:
        print("Number is greaater than 20")
else:
        print("Number is zero.")
