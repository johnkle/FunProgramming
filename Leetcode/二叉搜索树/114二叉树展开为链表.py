# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        if not root:
            return
        leftlist = self.flatten(root.left)
        rightlist = self.flatten(root.right)
        root.right = leftlist
        root.left = None
        tail = root
        while tail.right:
            tail = tail.right
        tail.right = rightlist
        return root
