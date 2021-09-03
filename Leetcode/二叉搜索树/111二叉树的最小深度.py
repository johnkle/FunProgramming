# 叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
# 当 root 节点左右孩子都为空时，返回 1
# 当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
# 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and root.right:
            return 1 
        depth = float('inf')
        if root.left:
            depth = min(self.minDepth(root.left),depth)
        if root.right:
            depth = min(self.minDepth(root.right),depth)
        return depth+1