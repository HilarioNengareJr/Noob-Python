"""
STACK IMPLEMENTATION
"""
class Stack:
    def __init__(self):
        """Constructs stack on object instantiation"""
        self.mxs = 100
        self.__stack = []
    
    def push(self,value):
        if len(self.__stack) < 100:
            self.__stack.append(value)
            print(f"{value} has been pushed")
        else:
            print("Stack Overflow!!")
            return
        
    def pop_(self):
        if len(self.__stack) == 0:
            print("Stack Underflow!!")
            return
        else:
            self.__stack.pop()
        
    def top(self):
        return (len(self.__stack)-1) #stack is 0 indexed
    
    def sizeofstack(self):
        return len(self.__stack)
    
    def traverse(self):
        i = 0
        while i < len(self.__stack):
            print(f"{i} -> {self.__stack[i]}")
            i=i+1
    

s = Stack()

s.push(456)
s.push(8_956)
s.push(5_485_785)
s.push(45)
s.pop_()
s.traverse()
print(f"The top index of stack is at {s.top()}")
print(f"The size of stack is {s.sizeofstack()}")

