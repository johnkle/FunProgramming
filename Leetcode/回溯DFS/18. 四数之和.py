class Solution:
    def fourSum(self, nums, target):
        res = []
        def dfs(nums,target,begin,path):
            if len(path)==4:
                if sum(path)==target:
                    res.append(path.copy())
                return
            for i in range(begin,len(nums)):
                # if len(nums) - i < 4 - len(path):
                #     return
                if i > begin and nums[i]==nums[i-1]:
                    continue
                if sum(path)+(4-len(path))*nums[i] > target:
                    return
                if sum(path)+(4-len(path))*nums[len(nums)-1] < target:
                    return
                path.append(nums[i])
                dfs(nums,target,i+1,path)
                path.pop()
        nums.sort()
        dfs(nums,target,0,[])
        return res