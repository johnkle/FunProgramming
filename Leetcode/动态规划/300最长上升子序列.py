# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)

class Solution2:
    def lengthOfLIS(self, nums):
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

if __name__ == "__main__":
    sl = Solution()
    lst = [2,3,7,101]
    print(sl.lengthOfLIS(lst))
