class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        def dfs(candidates,target,begin,path):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path.copy())
                return
            for i in range(begin,len(candidates)):
                if i>begin and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(candidates,target,i+1,path)
                path.pop()
        candidates.sort()
        dfs(candidates,target,0,[])
        return res