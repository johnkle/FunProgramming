class Solution:
    def combinationSum(self, candidates, target):
        if not candidates or target < 0:
            return []
        res = []
        def dfs(candidates,idx,path):
            if sum(path) == target:
                res.append(path.copy())
                return
            if sum(path) > target:
                return
            #注意搜索起点
            for i in range(idx,len(candidates)):
                #若当前元素和上一次选择的元素相同，则减枝
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                #从i开始选择下一层元素
                dfs(candidates,i,path)
                path.pop()
        candidates.sort()
        dfs(candidates,0,[])
        return res