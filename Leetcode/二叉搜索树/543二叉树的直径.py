class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #以node为根的二叉树的深度
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            #求深度过程中更新最大路径
            self.res = max(self.res,l+r+1)
            return max(l+1,r+1)
        dfs(root)
        return self.res-1