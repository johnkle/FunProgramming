#前序遍历所有路径，将符合条件的路径加入path，隐藏着回溯
#https://leetcode-cn.com/problems/path-sum-ii/solution/yi-pian-wen-zhang-jie-jue-suo-you-er-cha-oo63/
class Solution:
    def pathSum(self, root,sums):
        res = []
        def dfs(root,sums,path):
            if not root:
                return
            if not root.left and not root.right:
                if sum(path.copy()+[root.val]) == sums:
                    res.append(path.copy()+[root.val])
                return
            dfs(root.left,sums,path+[root.val])
            dfs(root.right,sums,path+[root.val])
        dfs(root,sums,[])
        return res

#回溯
class Solution:
    def pathSum(self, root, targetSum):
        res = []
        def dfs(root,targetSum,path):
            if not root:
                return
            if not root.left and not root.right:
                if sum(path.copy())+root.val == targetSum:
                    res.append(path.copy()+[root.val])
                return
            path.append(root.val)
            dfs(root.left,targetSum,path)
            dfs(root.right,targetSum,path)
            path.pop()
        dfs(root,targetSum,[])
        return res