#递归的将root路径加入到path
class Solution:
    def binaryTreePaths(self, root):
        res = []
        def dfs(root,path):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path+str(root.val))
                return
            dfs(root.left,path+str(root.val)+'->')
            dfs(root.right,path+str(root.val)+'->')
        dfs(root,'')
        return res

#回溯
class Solution:
    def binaryTreePaths(self, root):
        res = []
        def dfs(root,path):
            if not root:
                return
            if not root.left and not root.right:
                res.append('->'.join(path.copy()+[str(root.val)]))
                return
            path.append(str(root.val))
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()
        dfs(root,[])
        return res