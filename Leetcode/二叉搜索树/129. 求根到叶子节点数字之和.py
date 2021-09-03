#dfs搜索所有根到叶子的路径，对每一条路径表示的数字求和
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        self.res = 0
        def dfs(root,path):
            if not root:
                return
            path += str(root.val)
            if not root.left and not root.right:
                self.res += int(path)
                return
            dfs(root.left,path)
            dfs(root.right,path)
        dfs(root,'')
        return self.res

class Solution2(object):
    def sumNumbers(self, root):
        res = []
        def dfs(root,path):
            if not root:
                return
            #若到叶子节点，记录当前路径，回溯DFS
            if not root.left and not root.right:
                res.append(int(path+str(root.val)))
                return
            dfs(root.left,path+str(root.val))
            dfs(root.right,path+str(root.val))
        dfs(root,'')
        return sum(res)

