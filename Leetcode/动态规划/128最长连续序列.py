class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        dp = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                dp[i] = dp[i-1]+1
            elif nums[i] == nums[i-1]:
                dp[i] = dp[i-1]
            else:
                dp[i] = 1
        return max(dp)