#Linked_List
       
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    
    def __init__(self):
        self.head = None #make the head point to none for now
        
    def add_node(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head #make new node next as head
        self.head = new_node #make head point to new node
        
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
 
if __name__ == "__main__": #Main Program
    
    ll = Linked_List()
    
    a = Node(864584)
    b =  Node("hulas")
    
    ll.head = a
    a.next = b
    
    ll.add_node("hilario")#adds node at beginning of list
    
    ll.print_list()
    
    
    
    


