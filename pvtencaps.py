#represented by a double under_score __ltrl
class A:
    def __init__(self):
        self._name = 'hilario nengare' #protected
        self.__salary = '$250_000'  #private
        
    def accessor(self):
        print(f"Name is {self.name}")
        print(f"Salary is {self.salary}")
        
class B(A):
    def __init__(self):
        A.__init__(self) #calling Base ctor
        print(f"Name is {self._name}")
        print(f"Salary is {self._salary}") #error: attribute error
        
#inside main
a = A()
print(a._name) #prints protected name
#print(a.__salary)
b = B()#prints accessible data member
print(b._name) #accesses the protected data member

