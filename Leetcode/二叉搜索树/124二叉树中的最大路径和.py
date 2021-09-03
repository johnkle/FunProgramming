class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        #计算node的最大贡献值，并计算以node为根的最大路径和
        def helper(node):
            if not node:
                return 0
            leftGain = max(helper(node.left),0)
            rightGain = max(helper(node.right),0)
            path = node.val + leftGain + rightGain
            self.res = max(self.res,path)
            return node.val+max(leftGain,rightGain)
        helper(root)
        return self.res

class Solution2:
    def maxPathSum(self, root):
        res = []
        def dfs(node):
            if not node:
                return 0
            leftgain = max(dfs(node.left),0)
            rightgain = max(dfs(node.right),0)
            res.append(node.val+leftgain+rightgain)
            return node.val + max(leftgain,rightgain)
        dfs(root)
        return max(res)