#构造根节点，再递归构造左右子树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n):
        #左闭右闭，区间[left,right]所有可能的二叉搜索树
        def helper(left,right):
            if left>right:
                return [None]
            res = []
            for r in range(left,right+1):
                lefttrees = helper(left,r-1)
                righttrees = helper(r+1,right)
                for ltree in lefttrees:
                    for rtree in righttrees:
                        #注意构造根节点的位置
                        root = TreeNode(r)
                        root.left = ltree
                        root.right = rtree
                        res.append(root)
            return res
        return helper(1,n)

class Solution(object):
    def generateTrees(self, n):
        #左闭右开
        def helper(left,right):
            if left >= right:
                return [None]
            res = []
            for r in range(left,right):
                ltrees = helper(left,r)
                rtrees = helper(r+1,right)
                for lt in ltrees:
                    for rt in rtrees:
                        root = TreeNode(r)
                        root.left = lt
                        root.right = rt
                        res.append(root)
            return res
        return helper(1,n+1)