# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#递归
class Solution(object):
    def isValidBST(self, root):
        def helper(node,lower=float('-inf'),upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.left,lower,val):
                return False
            if not helper(node.right,val,upper):
                return False
            return True
        return helper(root)

class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node,lower=float('-inf'),upper=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return helper(node.left,lower,node.val)\
                and helper(node.right,node.val,upper)
        return helper(root)

#中序遍历
class Solution3:
    def isValidBST(self, root):
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return True