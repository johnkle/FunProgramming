class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        nodes = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        dfs(root)
        x = None
        y = None
        # todo 如何修改错换的值
        for i in range(len(nodes)-1):
            if nodes[i].val > nodes[i+1].val:
                y = nodes[i+1]
                if not x:
                    x = nodes[i]
        if x and y:
            x.val, y.val = y.val,x.val
        return root