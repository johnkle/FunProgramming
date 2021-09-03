#将0变为-1，问题转化为寻找和为0的最长连续子数组
class Solution:
    def findMaxLength(self, nums):
        record = dict()
        record[0] = -1
        pre = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
            pre += nums[i]
            if pre in record:
                res = max(res,i-record[pre])
            else:
                record[pre] = i
        return res