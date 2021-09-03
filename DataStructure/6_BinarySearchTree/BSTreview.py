from node import Node
class BST():
    def __init__(self):
        self.root = None
        self.size = 0
        self.L = []
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def add(self,node,e):
        if node is None:
            self.size += 1
            return Node(e)
        if e < node.e:
            node.left = self.add(node.left,e)
        if e > node.e:
            node.right = self.add(node.right,e)
        return node
    
    def contain(self,node,e):
        if node is None:
            return False
        if e == node.e:
            return True
        elif e < node.e:
            return self.contain(node.left,e)
        else:
            return self.contain(node.right,e)
    
    def findmax(self,node):
        if node.right is None:
            return node.e
        else:
            return self.findmax(node.right)
    
    def delmax(self,node):
        if node.right is None:
            self.leftnode = node.left
            node.left is None
            self.size-=1
            return self.leftnode
        node.right = self.delmax(node.right)
        return node
    
    def preorder(self,node):
        if node is None:
            return
        self.L.append(node.e)
        self.preorder(node.left)
        self.preorder(node.right)
    
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        self.L.append(node.e)
        self.inorder(node.right)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        self.L.append(node.e)

        
