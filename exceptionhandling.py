#raise invokes an error based off of input
#or it may be based off a condition for example
#e/g if user enters a certain value that is not what we want we can raise an exception to it

def is_odd(number):
    if not isinstance(number,int):
        raise TypeError("The symbol is not an integer!")
    if number % 2 == 0:
        raise ValueError("The number entered is not an odd number!!")
