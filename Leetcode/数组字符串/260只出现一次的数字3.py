import collections
class Solution:
    def singleNumber(self, nums):
        hashmap = collections.Counter(nums)
        res = []
        for k in hashmap.keys():
            if hashmap[k] == 1:
                res.append(k)
        return res