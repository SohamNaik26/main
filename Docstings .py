def square(n):
    ''' Takes in a number n, returns the square of n'''
    print(n ** 2)
square(5)
print(square.__doc__)


def add(num1, num2):
    """ Add up to two numbers. This function simply wraps the ''+'' operator, and does not do anything interesting, /n except for illustrating what the Docstring of a very simple function looks like. Parameters  ----------  num1 : int First number to add.num2 : int Second number to add. """
    print(num1 + num2)
add(12, 25)
print(add.__doc__) 
