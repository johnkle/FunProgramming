class Solution:
    def findSubsequences(self, nums):
        res = []
        def dfs(nums,begin,path):
            if len(path) >= 2:
                if path[-1] >= path[-2]:
                    if path not in res:
                        res.append(path.copy())
                else:
                    return
            for i in range(begin,len(nums)):
                if i > begin and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(nums,i+1,path)
                path.pop()
        dfs(nums,0,[])
        return res