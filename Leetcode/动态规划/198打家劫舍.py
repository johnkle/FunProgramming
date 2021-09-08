class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2,len(nums)):
            for j in range(i-1):
                dp[i] = max(dp[i],dp[j]+nums[i])
        return max(dp)

class Solution2:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        #dp[i][0]盗取第i间房获得的最高金额，dp[i][1]不盗取第i间房获得的最高金额
        dp = [[0,0] for _ in range(len(nums))]
        dp[0] = [nums[0],0]
        for i in range(1,len(dp)):
            dp[i][0] = dp[i-1][1]+nums[i]
            dp[i][1] = max(dp[i-1])
        return max(dp[-1])

class Solution3(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[len(nums)-1]