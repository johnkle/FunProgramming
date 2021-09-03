#参523 前缀和
class Solution:
    def subarraysDivByK(self, nums, k):
        record = dict()
        record[0] = 1
        remainder = 0
        count = 0
        for i in range(len(nums)):
            remainder = (remainder+nums[i])%k
            if remainder in record:
                count += record[remainder]
                record[remainder] += 1
            else:
                record[remainder] = 0
                record[remainder] += 1
        return count

class Solution2:
    def subarraysDivByK(self, nums, k):
        record = dict()
        record[0] = 1
        remainder = 0
        count = 0
        for i in range(len(nums)):
            remainder = (remainder+nums[i])%k
            same = record.get(remainder,0)
            count += same
            record[remainder] = same+1
        return count