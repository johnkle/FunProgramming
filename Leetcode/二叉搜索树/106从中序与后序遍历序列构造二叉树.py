# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        def helper(in_left,in_right,post_left,post_right):
            if in_left > in_right:
                return
            post_root = post_right
            in_root = inorder.index(postorder[post_root])
            root = TreeNode(inorder[in_root])
            size_left_subtree = in_root-in_left
            root.left = helper(in_left,in_root-1,post_left,post_left+size_left_subtree-1)
            root.right = helper(in_root+1,in_right,post_left+size_left_subtree,post_right-1)
            return root
        return helper(0,len(inorder)-1,0,len(postorder)-1)

class Solution2(object):
    def buildTree(self, inorder, postorder):
        def helper(in_left,in_right):
            if in_left > in_right:
                return
            root_val = postorder.pop()
            in_root_index = inorder.index(root_val)
            root = TreeNode(root_val)
            root.right = helper(in_root_index+1,in_right)
            root.left = helper(in_left,in_root_index-1)
            return root
        return helper(0,len(inorder)-1)

class Solution3(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx],postorder[:idx])
        root.right =self.buildTree(inorder[idx+1:],postorder[idx:-1])
        return root