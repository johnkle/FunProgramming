class Solution:
    def combine(self,n, k):
        res = []
        if k<=0 or n<k:
            return res
        def dfs(n,k,begin,path):
            if len(path) == k:
                res.append(path.copy())
                return
            #注意搜索起点
            for i in range(begin,n):
                path.append(i+1)
                dfs(n,k,i+1,path)
                path.pop()
        dfs(n,k,0,[])
        return res