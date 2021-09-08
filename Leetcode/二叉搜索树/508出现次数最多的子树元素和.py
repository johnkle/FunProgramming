import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = collections.Counter()
    def findFrequentTreeSum(self, root):
        #求以node为根的子树元素和
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.res[l+r+node.val] += 1
            return node.val + l + r
        dfs(root)
        temp = self.res.most_common(1)[0][0]
        ans = []
        for node in self.res:
            if self.res[node] == self.res[temp]:
                ans.append(node)
        return ans