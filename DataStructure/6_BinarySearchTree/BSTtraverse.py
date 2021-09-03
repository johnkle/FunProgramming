class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def preOrder1(self,node):
        L=[]
        if node==None:
            return
        L.append(node.val)
        self.preOrder1(node.left)
        self.preOrder1(node.right)
    #用栈记录将要访问的节点
    def preOrder2(self,node):
        stack = []
        stack.append(node)
        while stack is not None:
            self.cur = stack.pop(node)
            print(self.cur.val)
            if self.cur.right is not None:
                stack.append(self.cur.right)
            if self.cur.left is not None:
                stack.append(self.cur.left)

    #用队列记录将要访问的节点  
    def levelorder(self,node):
        queue = []
        queue.append(node)
        while queue is not None:
            self.cur = queue.pop(0)
            print(self.cur.val)
            if self.cur.left is not None:
                queue.append(self.cur.left)
            if self.cur.right is not None:
                queue.append(self.cur.right)