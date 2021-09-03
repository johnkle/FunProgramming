class Solution:
    def permuteUnique(self, nums):
        if not nums:
            return []
        res = []
        path = []
        used = [0]*len(nums)
        def backtrack(nums,path,used):
            if len(path) == len(nums):
                #注意是path.copy()
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums,path,used)
                path.pop()
                used[i] = 0
        nums.sort()
        backtrack(nums,path,used)
        return res

class Solution2:
    def permuteUnique(self, nums):
        res = []
        used = [0]*len(nums)
        def dfs(nums,level,path):
            if level == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                #去重
                if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
                    continue
                used[i] = 1
                path.append(nums[i])
                dfs(nums,level+1,path)
                path.pop()
                used[i] = 0
        #排序
        nums.sort()
        dfs(nums,0,[])
        return res