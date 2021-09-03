class Solution:
    def jump(self, nums):
        dp = [float("inf") for _ in range(len(nums))]
        dp[0] = 0
        for i in range(1,len(dp)):
            for j in range(i):
                if nums[j] < i-j:
                    continue
                dp[i] = min(dp[i],dp[j]+1)
        print(dp)
        return dp[-1]

#如何贪心解决