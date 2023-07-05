def calculateGmean(a, b):
    mean = (a * b)/(a + b)
    print(mean)

def isGreater(a, b):
    if(a > b):
        print("First numaber is greater")
    else:
        print("Second number is greater")

def islesser(a,b):
    pass

a = 9
b = 8
isGreater(a, b)

calculateGmean(a, b)

c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)

def percent(marks):
    p = ((marks[0] + marks[1] +marks[3])/400)*100
    return p

marks1 =  [98, 75, 64, 83]
percentage1 = percent(marks1)

marks2 = [75, 955, 80, 59]
percentage2 = percent(marks2)
print(percentage1, percentage2)
