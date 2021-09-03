# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root):
        def isValid(node,lower,upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return isValid(node.left,lower,node.val) and isValid(node.right,node.val,upper)
        def count(node):
            if not node:
                return 0
            return count(node.left)+count(node.right)+1
        if not root:
            return 0
        if isValid(root,float('-inf'),float('inf')):
            return count(root)
        return max(self.largestBSTSubtree(root.left),self.largestBSTSubtree(root.right))