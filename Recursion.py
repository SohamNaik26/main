# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(0) = 1

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
print(factorial(4))
print(factorial(5))

# Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n - 2)

def f(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(4))
print(f(6))
print(f(7))