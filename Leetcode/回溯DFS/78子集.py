class Solution:
    def subsets(self, nums):
        res = []
        def dfs(nums,begin,path):
            if len(path)<=len(nums):
                res.append(path.copy())
                if len(path) == len(nums):
                    return
            for i in range(begin,len(nums)):
                path.append(nums[i])
                dfs(nums,i+1,path)
                path.pop()
        dfs(nums,0,[])
        return res