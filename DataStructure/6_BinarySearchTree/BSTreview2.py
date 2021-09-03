class Node():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        self.size = 0
        self.L = []
    def getSize(self):
        return self.size
    
    def add(self,val):
        return self._add(self.root,val)
    def _add(self,node,val):
        if node is None:
            return Node(val)
        if val < node.val:
            node.left = self._add(node.left,val)
        if val > node.val:
            node.left = self._add(node.right,val)
        return node
        
    def contain(self,node,val):
        if node is None:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self.contain(node.left,val)
        if val > node.val:
            return self.contain(node.right,val)
    def findmax(self,node):
        if node.right is None:
            return node.val
        return self.findmax(node.right)
    def delemax(self,node):
        if node.right is None:
            self.leftnode = node.left
            node.left = None
            return self.leftnode
        node.right = self.delemax(node.right)
        return node
    def preorder1(self,node):
        self.L.append(node.val)
        self.preorder1(node.left)
        self.preorder1(node.right)
    def preorder2(self,node):
        self.stack = []
        self.stack.append(node)
        while self.stack is not None:
            self.cur = self.stack.pop()
            if node.right is not None:
                self.stack.append(node.right)
            if node .left is not None:
                self.stack.append(node.left)
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        self.L.append(node.val)
        self.inorder(node.right)
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        self.L.append(node.val)
    def levelorder(self,node):
        self.queue = []
        self.queue.append(node)
        while self.queue is not None:
            self.cur = self.queue[0]
            print(self.cur.val)
            if node.left is not None:
                self.queue.append(node.left)
            if node.right is not None:
                self.queue.append(node.right)
        
#test code
bst = BST()
for i in range(1,12):
    bst.add(i)


        