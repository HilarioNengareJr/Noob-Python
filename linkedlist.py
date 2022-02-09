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
    
    def add_in(self,old_node,d):
        """ Pass old node as demarcation and the value of the new node """
        mid_node = Node(d)
        mid_node.next = old_node.next #make the mid node to point to whatever the node was pointing to
        old_node.next = mid_node #then make the old_node point
    
    def add_last(self,the_data):#add node at the end of the list
        end_node = Node(the_data)
        tvs = self.head
        
        if(tvs == None):
            print("No Nodes Prior! Error.")
            return
        
        while(tvs.next):
            tvs = tvs.next
        #when while loop fails then add the node at the last site
        tvs.next = end_node
        
        
    def print_list(self):
        temp = self.head #no name conflicts between temp, previous temp died when its block ended
        while(temp):
            print(temp.data)
            temp = temp.next
 
if __name__ == "__main__": #Main Program
    
    ll = Linked_List()
    
    #Instantiate/Initialize
    a = Node(864584)
    b =  Node("hulas")
    
    #Link up
    ll.head = a
    a.next = b
    
    ll.add_node("hilario")#adds node at beginning of list
    ll.add_in(a,678)
    ll.add_last(456)#adds node at the last site
    
    ll.print_list()
    
    
    
    



