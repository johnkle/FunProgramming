#dp[i]表示以nums[i]结尾的最大整除子集
class Solution(object):
    def largestDivisibleSubset(self, nums):
        #先排序
        nums.sort()
        res = [nums[0]]
        dp = [[nums[i]] for i in range(len(nums))]
        dp[0] = [nums[0]]
        for i in range(1,len(dp)):
            for j in range(i):
                #如果nums[i]能跟在nums[j]后面,更新dp[i]
                if nums[i]%nums[j] == 0 and len(dp[j])+1>len(dp[i]):
                    dp[i] = dp[j]+[nums[i]]
            #每遍历一个i，更新res
            if len(dp[i]) > len(res):
                res = dp[i]
        # for i in range(len(dp)):
        #     if len(dp[i]) > len(res):
        #         res = dp[i]
        return res