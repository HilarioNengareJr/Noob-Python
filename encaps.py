# Python program to
# demonstrate protected members
#Protected members in python are denoted with/by/using a single under-score e/g _ltrl
#protected members are accessible out of the class even in the derived classes but please bro refrain from doing so outside of the classesssssssss
 
# Creating a base class
class A:
    def __init__(self):
 
        # Protected member
        self._num = 20
 
# Creating a derived class
class B(A):
    def __init__(self):
 
        # Calling constructor of
        # Base class A
        A.__init__(self)
        print("Calling protected member of A: ",
              self._num)
 
        # Modify the protected variable:
        self._num = 30
        print("Calling modified protected member outside class: ",
              self._num)
 
 
b = B()
 
a = A()
 
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of b: ", a._num)
 
# Accessing the protected variable outside
print("Accessing protedted member of obj2: ", a._num)
