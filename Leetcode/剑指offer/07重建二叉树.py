# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(pre_left,pre_right,in_left,in_right):
            if pre_left > pre_right:
                return
            pre_root = pre_left
            in_root = index(preorder(pre_root))
            left_size = in_root - in_left
            root = TreeNode(preorder(pre_root))
            root.left = helper(pre_left+1,pre_left+left_size,in_left,in_root-1)
            root.right = helper(pre_left+size_left+1,pre_right,in_root+1,in_right)
        return helper(0,n-1,0,n-1)