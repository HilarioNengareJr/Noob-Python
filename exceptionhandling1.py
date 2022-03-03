#we can have the try and except clause catch errors within a misbehaving chunk of code
#and then it can continue running without a crush being caused by the misbehaving chunk of code
#e.g no_return() is faulty but the except will work fine 

def no_return():
    print("I am about to catch an exception")
    raise Exception("This will always be raised")
    return("Won't execute!")

try:
    no_return()
except:
    print("I am printed")
print("Hello World")

#if we were writing some code that could raise both a TypeError and a 
#ZeroDivisionError

def div(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        return "0 is not a good idea dawg"
        
print(div(0))
print(div(56))
#print(div("a")) #propagates a typeerror to the console

#we can catch more errors with same clause
def div_t(divider):
    try:
        if divider == 7:
            raise ValueError("7 is an unlucky number")
        return 100/divider
    except (ZeroDivisionError,TypeError):
        return "Anything else besides 0"
    
for i in [4,56,0,"h",7]:
    print("Testing {}:".format(i), end=" ")
    print(div_t(i))