"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
并返回其长度。如果不存在符合条件的连续子数组，返回 0。
"""

class Solution1(object):
    def minSubArrayLen(self, s, nums):
        sums = 0
        res = len(nums)+1
        left = 0
        right = 0
        while right <= len(nums)-1:
            sums += nums[right]
            while sums>=s:
                res = min(res,right-left+1)
                sums -= nums[left]
                left += 1
            right += 1
        return res if res!=len(nums)+1 else 0

class Solution2(object):
    def minSubArrayLen(self, s, nums):
        res =len(nums)+1
        left = 0
        right = 0
        while right <= len(nums)-1:
            while sum(nums[left:right+1]) >= s:
                res = min(res,right-left+1)
                left += 1
            right += 1
        return res if res!=len(nums)+1 else 0



if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    s = 7
    s2 = Solution2()
    print(s2.minSubArrayLen(s,nums))
