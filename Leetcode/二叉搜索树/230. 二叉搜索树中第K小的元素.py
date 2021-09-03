# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res[k-1]

class Solution2:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = 0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res

class Solution3(object):
    def kthSmallest(self, root, k):
        def inorder(root):
            return inorder(root.left)+[root.val]+inorder(root.right) if root else []
        return inorder(root)[k-1]