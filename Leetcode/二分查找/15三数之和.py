class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    item = [nums[i],nums[left],nums[right]]
                    if not item in res:
                        res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif temp < 0:
                    left += 1
                else:
                    right -= 1
        return res

#回溯DFS，超时，参考39组合总和
class Solution2:
    def threeSum(self, nums):
        nums.sort()
        res = []
        def dfs(nums,pos,idx,path):
            if idx > 3:
                return
            if idx==3 and sum(path)==0:
                res.append(path.copy())
                return
            for i in range(pos,len(nums)):
                #剪枝
                if i>pos and nums[i]==nums[i-1]:
                    continue
                if idx==0 and nums[i]>0:
                    continue
                path.append(nums[i])
                dfs(nums,i+1,idx+1,path)
                path.pop()
        dfs(nums,0,0,[])
        return res

if __name__ == "__main__":
    sl = Solution2()
    nums = []
    print(sl.threeSum(nums))