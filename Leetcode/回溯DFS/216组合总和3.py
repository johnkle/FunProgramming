class Solution:
    def combinationSum3(self, k, n):
        res = []
        def dfs(k,n,begin,path):
            if len(path)>k or sum(path)>n:
                return
            if len(path)==k and sum(path)==n:
                res.append(path.copy())
                return
            for i in range(begin,10):
                path.append(i)
                dfs(k,n,i+1,path)
                path.pop()
        dfs(k,n,1,[])
        return res

class Solution2:
    def combinationSum3(self, k, n):
        res = []
        def dfs(k,n,begin,path):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path.copy())
                return
            for i in range(begin,10):
                path.append(i)
                dfs(k,n,i+1,path)
                path.pop()
        dfs(k,n,1,[])
        return res