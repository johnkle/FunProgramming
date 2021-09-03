class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class binarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0
        self.res = []
    
    def add(self,e):
        def _add(node,e):
            if node is None:
                return Node(e)
            if e < node.val:
                node.left = _add(node.left,e)
            elif e > node.val:
                node.right = _add(node.right,e)
            return node
        self.root = _add(self.root,e)

    def contain(self,e):
        def _contain(node,e):
            if node is None:
                return False
            if e == node.val:
                return True
            if e < node.val:
                return _contain(node.left,e)
            if e > node.val:
                return _contain(node.right,e)
        return _contain(self.root,e)

    def replace(self,p,q):
        def _replace(node,p,q):
            if node is None:
                return
            if p == node.val:
                node.val = q
                return
            elif p < node.val:
                _replace(node.left,p,q)
            else:
                _replace(node.right,p,q)
        _replace(self.root,p,q)

    def preOrder(self):
        def _preOrder(node):
            if node is None:
                return
            self.res.append(node.val)
            _preOrder(node.left)
            _preOrder(node.right)
        return _preOrder(self.root)

    def preOrder1(self):
        def _preOrder1(node):
            if node is None:
                return
            stack = []
            stack.append(node)
            while stack is not None:
                self.cur = stack.pop()
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    stack.append(node.left)
        return _preOrder1(self.root)

    def levelOrder(self):
        def _levelOrder(node):
            if node is None:
                return
            queue = []
            queue.append(node)
            while queue is not None:
                self.cur = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return _levelOrder(self.root)
    
#删除以node为根的二分搜索树中的最大节点
#返回删除节点后新的二分搜索树的根
    def removeMax(self):
        def _removeMax(node):
            if node.right is None:
                leftnode = node.left
                node.left = None
                return leftnode
            node.right = _removeMax(node.right)
        return _removeMax(self.root)

    def findMax(self):
        return self._findMax(self.root)
    def _findMax(self,node):
        if node.right is None:
            return node
        return self._findMax(node.right)
