#前缀和+hashMap
class Solution:
    def subarraySum(self, nums, k):
        record = dict()
        record[0] = 1
        pre = 0
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre-k in record:
                count += record[pre-k]
            if pre not in record:
                record[pre] = 0
            record[pre] += 1
        return count


