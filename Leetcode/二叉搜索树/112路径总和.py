# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left,sum-root.val)\
            or self.hasPathSum(root.right,sum-root.val)

#思路，dfs搜索路径
class Solution2:
    def hasPathSum(self, root, sum):
        def dfs(root,path):
            if not root:
                return False
            if not root.left and not root.right:
                return path+root.val == sum
            return dfs(root.left,path+root.val) or dfs(root.right,path+root.val)
        return dfs(root,0)

class Solution3:
    def hasPathSum(self, root, sums) -> bool:
        def dfs(root,sums,path):
            if not root:
                return False
            if not root.left and not root.right:
                return sum(path+[root.val])==sums
            return dfs(root.left,sums,path+[root.val]) or dfs(root.right,sums,path+[root.val])
        return dfs(root,sums,[])