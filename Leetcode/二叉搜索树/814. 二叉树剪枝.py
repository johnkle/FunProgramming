class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root):
        #判断node是不是全为0
        def dfs(node):
            if not node:
                return True
            return node.val == 0 and dfs(node.left) and dfs(node.right)
        #先判断根节点
        if dfs(root):
            root = None
            return root
        #递归的剪除左右子树
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root

class Solution:
    def pruneTree(self, root):
        #dfs过程中做一些事
        def dfs(node):
            if not node:
                return True
            l = dfs(node.left)
            r = dfs(node.right)
            if l:
                node.left = None
            if r:
                node.right = None
            return node.val == 0 and dfs(node.left) and dfs(node.right)
        return None if dfs(root) else root