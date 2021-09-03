class BST():
    class node():
        def __init__(self,key,value,left=None,right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
    
    def insert(self,node,key,value):
        if self.node == None:
            return key,value
        if key == node.key:
            node.key = key
        elif key < node.key:
            self.insert(node.left,key,value)
        elif key > node.key:
            self.insert(node.right,key,value)
        
