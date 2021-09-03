class Solution(object):
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root):
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res