classes

class Employee:
    """ A class demonstration using python """
    s = 300_000
     
    #constructor to take in name of employee
    def __init__(self,firstname,lastname): #method
        self.firstname = firstname
        self.lastname = lastname
        
    def get_details(self):
        return self.firstname, self.lastname, self.s
    
    # Destructor.. but is handled automatically by the garbage collector
    def __del__(self):
        pass

class Manager(Employee):
    """ Derived class of Employee """
    
    def get_salary(self):
        return self.s * 2

name = input('')
secname = input('')
m = Manager(name,secname)
print(m.get_salary)
#e = Employee(name,secname)
#print(e.get_details())
