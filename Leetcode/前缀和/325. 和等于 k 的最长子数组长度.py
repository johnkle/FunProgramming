class Solution:
    def maxSubArrayLen(self, nums, k):
        record = dict()
        record[0] = -1
        pre = 0
        res = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre-k in record:
                res = max(res,i-record[pre-k])
            if pre not in record:
                record[pre] = i
        return res