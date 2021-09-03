# 给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。

class Solution(object):
    def findLengthOfLCIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        return max(dp)

if __name__ == "__main__":
    sl = Solution()
    s = [1,3,5,8,6]
    print(sl.findLengthOfLCIS(s))
                