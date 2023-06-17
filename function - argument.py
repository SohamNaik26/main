def average(a = 9, b = 1):
    print("The average is ", (a + b)/2)

# average(4, 6)
average(b = 9, a = 21)

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name( "LXI", "MOV", "MVI")

average(5, 6)

def average (*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
     #   print("The average is:", sum / len(numbers))
    return 7
    return sum / len(numbers)


average(5, 6, 7 ,1)