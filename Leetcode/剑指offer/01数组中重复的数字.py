class Solution(object):
    def findRepeatNumber(self, nums):
        temp = set()
        for x in nums:
            if x in temp:
                return x
            temp.add(x)