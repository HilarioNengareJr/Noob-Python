#functions in  python
def employee(first_name, last_name):
    print(first_name, last_name)
   #keyword args
employee(first_name = 'hilario',last_name = 'nengare')

#variable-length arguments
def adder(*argv):
    """*args for variable number of arguments""" #docstring
    result = 0 
    for arg in argv:
        result += arg
        
    return result

print(adder(5,4,5,87,4,6,89))


def fibonacci(n):
    
    if n < 2 and n > -1:
        return n
    else:
        return n-1+n-2
    
print(fibonacci(8))

fib = lambda m:m-1+m-2

print(fib(8))

