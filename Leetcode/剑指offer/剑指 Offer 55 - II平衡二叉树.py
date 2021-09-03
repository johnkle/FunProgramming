# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return abs(leftDepth-rightDepth)<=1 and\
            self.isBalanced(root.left) and self.isBalanced(root.right)
    def maxDepth(self,root):
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1