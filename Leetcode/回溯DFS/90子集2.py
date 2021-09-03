class Solution:
    def subsetsWithDup(self, nums):
        res = []
        def dfs(nums,begin,path):
            if len(path)<=len(nums):
                res.append(path.copy())
                if len(path) == len(nums):
                    return
            for i in range(begin,len(nums)):
                if i > begin and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(nums,i+1,path)
                path.pop()
        nums.sort()
        dfs(nums,0,[])
        return res