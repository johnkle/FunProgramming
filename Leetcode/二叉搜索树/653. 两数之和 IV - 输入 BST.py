# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k):
        lookup = set()
        def dfs(node,k):
            if not node:
                return False
            if k-node.val in lookup:
                return True
            lookup.add(node.val)
            return dfs(node.left,k) or dfs(node.right,k)
        return dfs(root,k)