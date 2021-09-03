#最大子序和 连续
class Solution(object):
    def maxSubArray(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)

#最大子序和 不连续
def func(nums):
    dp = [nums[i] for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            dp[i] = max(dp[j]+nums[i],dp[i])
    print(dp)
    return max(dp)

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(func(nums))
