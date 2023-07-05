# n = 1 * 2 * 3 * 4 .... * n

# n = 4
# product = 1
# for i in range(n):
#     product = product * (i + 1)
#     print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)
    
# f = factorial_iter(5)
f = factorial_recursive(5)
print(f)

def maximum(num1, num2, num3):
    if (num1 > num2):
        if(num1 > num3):
            return num1
    
    else:
        if (num2>num3):
            return num2
    
        else:
            return num3
m = maximum(3, 5, 35)
print("The value of the maximum is " + str(m))