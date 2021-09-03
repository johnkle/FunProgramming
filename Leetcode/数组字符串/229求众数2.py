import collections
class Solution(object):
    def majorityElement(self, nums):
        hashmap = collections.Counter(nums)
        n = len(nums)//3
        res = []
        for k in hashmap:
            if hashmap[k]>n:
                res.append(k)
        return res

sl = Solution()
nums = [1,1,1,3,3,2,2,2]
res = sl.majorityElement(nums)
print(res)