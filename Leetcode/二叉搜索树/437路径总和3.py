# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def pathSum(self, root, sums):
        #以node为根的和为sums的所有路径
        def dfs(node,sums):
            if not node:
                return
            if node.val == sums:
                self.res += 1
                #不要return，不是到叶子节点结束，可能还有一条路经下还有其他路径
            dfs(node.left,sums-node.val)
            dfs(node.right,sums-node.val)

        if not root:
            return 0
        dfs(root,sums)
        self.pathSum(root.left,sums)
        self.pathSum(root.right,sums)
        return self.res

#dfs
class Solution2:
    def __init__(self):
        self.res = 0
    def pathSum(self, root, sums):
        def dfs(node,sums,path):
            if not node:
                return
            if path+node.val == sums:
                self.res += 1
            dfs(node.left,sums,path+node.val)
            dfs(node.right,sums,path+node.val)
        if not root:
            return 0
        dfs(root,sums,0)
        self.pathSum(root.left,sums)
        self.pathSum(root.right,sums)
        return self.res

#回溯
class Solution2b:
    def __init__(self):
        self.res = 0
    def pathSum(self, root, sums):
        def dfs(node,sums,path):
            if not node:
                return
            if path+node.val == sums:
                self.res += 1
            path += node.val
            dfs(node.left,sums,path)
            dfs(node.right,sums,path)
            path -= node.val
        if not root:
            return 0
        dfs(root,sums,0)
        self.pathSum(root.left,sums)
        self.pathSum(root.right,sums)
        return self.res

#找出所有路径 超时
class Solution3:
    def __init__(self):
        self.res = []
    def pathSum(self, root, sums):
        def dfs(node,sums,path):
            if not node:
                return
            if sum(path.copy()+[node.val]) == sums:
                self.res.append(path.copy()+[node.val])
            dfs(node.left,sums,path+[node.val])
            dfs(node.right,sums,path+[node.val])
        if not root:
            return 0
        dfs(root,sums,[])
        self.pathSum(root.left,sums)
        self.pathSum(root.right,sums)
        return self.res

#递归
class Solution4:
    def __init__(self):
        self.res = 0
    def pathSum(self, root,sums):
        def dfs(node,sums):
            if not node:
                return
            if node.val == sums:
                self.res += 1
            dfs(node.left,sums-node.val)
            dfs(node.right,sums-node.val)
        if not root:
            return 0
        dfs(root,sums)
        self.pathSum(root.left,sums)
        self.pathSum(root.right,sums)
        return self.res


