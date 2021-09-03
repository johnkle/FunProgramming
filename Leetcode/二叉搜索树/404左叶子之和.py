class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#深度优先，前序遍历
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        isLeaf = lambda node: not node.left and not node.right
        res = []
        def dfs(root):
            if not root:
                return
            if root.left and isLeaf(root.left):
                res.append(root.left.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return sum(res)