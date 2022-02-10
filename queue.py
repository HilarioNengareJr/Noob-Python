#queue
      #is kind of slow...after a pop elements have to be shifted by one
#can use collections.deque has utilies to append and/or pop from both ends

class Q:
    """ implementation of the class Queue class """
    
    def __init__(self,max_size):
        self.max_size = max_size
        self.mylist = [] * self.max_size
        
    def Enqueue(self, data):
        if len(self.mylist) == self.max_size-1:
            print("Queue is full")
            return
        
        else:
            self.mylist.append(data)
    
    def Dequeue(self):
        if len(self.mylist) == 0:
            print("No dequeue operation is capable!!")
            return
        
        else:
            self.mylist.pop(0) #remove the first element to be appended
            
    def Display(self):
        for i in self.mylist:
            print(i)
            
if __name__ == "__main__":
    
    q = Q(3)
    q.Enqueue(456_789)
    q.Enqueue(345)
    q.Display()
    
    
