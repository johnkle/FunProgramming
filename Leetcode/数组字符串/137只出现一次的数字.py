import collections
class Solution:
    def singleNumber(self, nums):
        lookup = collections.Counter(nums)
        for x in nums:
            if lookup[x] == 1:
                return x

class Solution2:
    def singleNumber(self, nums):
        for x in nums:
            if nums.count(x)==1:
                return x