class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        #搜索每个节点不偷或偷的最高金额[notrobbed,robbed]
        def dfs(node):
            if not node:
                return [0,0]
            l = dfs(node.left)
            r = dfs(node.right)
            notrobbed = max(l) + max(r)
            robbed = node.val + l[0] + r[0]
            return [notrobbed,robbed]
        return max(dfs(root))