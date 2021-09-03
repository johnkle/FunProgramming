#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
        l = self.pathSum(root.left,sum-root.val)
        r = self.pathSum(root.right,sum-root.val)
        return [[root.val]+lst for lst in l+r]

