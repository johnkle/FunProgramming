#如果是0-1背包，即数组中的元素不可重复使用，nums放在外循环，target在内循环，且内循环倒序
class Solution:
    def canPartition(self, nums):
        if len(nums) < 2:
            return False
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target,num-1,-1):
                dp[i] |= dp[i-num]
        return dp[-1]