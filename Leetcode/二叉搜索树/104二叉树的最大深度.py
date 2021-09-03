class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        depth = float('-inf')
        if root.left:
            left_depth = self.maxDepth(root.left)
        if root.right:
            right_depth = self.maxDepth(root.right)
        return max(left_depth,right_depth)+1