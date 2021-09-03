# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root):
        if not root:
            return root
        if not root.left and not root.right:
            return root
        leftnode = root.left
        newhead = self.upsideDownBinaryTree(root.left)
        leftnode.left = root.right
        leftnode.right = root
        root.left = None
        root.right = None
        return newhead