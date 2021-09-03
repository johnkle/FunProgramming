#同于定理 在record中查询是否存在前缀和的余数与当前索引前缀和余数相同，若相等，则两者只差可被k整除
#参974
class Solution:
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False
        record = dict()
        record[0] = -1
        remainder = 0
        for i in range(len(nums)):
            remainder = (remainder+nums[i])%k
            if remainder in record:
                idx = record[remainder]
                if i-idx > 1:
                    return True
            else:
                record[remainder] = i
        return False


