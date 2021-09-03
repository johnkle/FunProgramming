#先序找根，划分左右，再递归构造左右子树
#关键是确定根节点，然后递归的构造左子树和右子树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(pre_left,pre_right,in_left,in_right):
            if pre_left > pre_right:
                return
            pre_root = pre_left
            in_root = inorder.index(preorder[pre_root])
            root = TreeNode(preorder[pre_root])
            size_left_subtree = in_root - in_left
            root.left = helper(pre_left+1,pre_left+size_left_subtree,in_left,in_root-1)
            root.right = helper(pre_left+size_left_subtree+1,pre_right,in_root+1,in_right)
            return root
        return helper(0,len(preorder)-1,0,len(inorder)-1)


class Solution2:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        idx = inorder.index(preorder[0])  # 中序为“左根右”，idx为左+根的长度，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root


