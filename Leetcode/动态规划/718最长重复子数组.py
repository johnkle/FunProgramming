#参考最长公共子串
class Solution:
    def findLength(self, nums1, nums2):
        row = len(nums1)
        col = len(nums2)
        res = 0
        dp = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    res = max(res,dp[i][j])
        return res