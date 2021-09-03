class Solution:
    def rob(self, nums):
        def helper(nums):
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            #dp[i] 偷窃前i间房屋得到的最高金额
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        # 注意初始状态和打家劫舍1的不同
        if len(nums) < 3:
            return max(nums)
        return max(helper(nums[:-1]),helper(nums[1:]))

class Solution:
    def rob(self, nums):
        def helper(nums):
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            # dp[i] 偷窃前i间房屋得到的最高金额(包括nums[i])
            for i in range(2,len(nums)):
                for j in range(i-1):
                    dp[i] = max(dp[i],dp[j]+nums[i])
            return max(dp)
        if len(nums) < 3:
            return max(nums)
        return max(helper(nums[:-1]),helper(nums[1:]))