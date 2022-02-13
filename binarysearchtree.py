# Binary Search Tree and Recursion

class BST:
    """ implementation of the BINARY SEARCH TREE class """
    
    def __init__(self,data):
        self.val = data
        self.left_node = None
        self.right_node = None
    
def insert_bst(root, data):
    if root is None:
        return BST(data)
    elif root.val == data:
        return root
    elif root.val < data:
        root.left_node = insert_bst(root.left_node,data)
    else:
        root.right_node = insert_bst(root.right_node,data)
    return root
    
def traverse_bst(Node):
    if Node is None:
        return
    traverse_bst(Node.left_node)
    print(Node.val)
    traverse_bst(Node.right_node)
   
if __name__ == "__main__":
    
    # instantiate an object of BST
    bst = BST(890)
    bst = insert_bst(bst,678)
    bst = insert_bst(bst,980)
    traverse_bst(bst)
    
    
    
