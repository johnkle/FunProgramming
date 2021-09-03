class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        def inorder(root):
            if not root:
                return
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        inorder(root)
        return self.res