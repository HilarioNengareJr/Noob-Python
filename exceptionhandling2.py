import random

some_exceptions = [TypeError,ValueError,IndexError,None]

def name_me(variable):
    return "{} how are you?".format(variable)
try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error has resulted.")
except TypeError:
    print("Raising a TypeError")
    
except ValueError:
    print("Raising a ValueError")
    
except IndexError:
    print("Raising IndexError")

else: #part of the code that will execute
    print("I survived the errors")
    
finally:
    """
the finally clause is executed no matter what 
happens. This is extremely useful when we need to perform certain tasks after 
our code has finished running (even if an exception has occurred). Some common 
examples include:
• Cleaning up an open database connection
• Closing an open file
• Sending a closing handshake over the network"""
    print(name_me("hilario"))
    