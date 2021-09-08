class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.res = 0
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            # if not node.left and not node.right:
            #     return 1
            temp = 1
            l = dfs(node.left)
            r = dfs(node.right)
            if node.left and (node.val+1 == node.left.val):
                temp = max(temp,l+1)
            if node.right and (node.val+1 == node.right.val):
                temp = max(temp,r+1)
            self.res = max(self.res,temp)
            return temp
        dfs(root)
        return self.res