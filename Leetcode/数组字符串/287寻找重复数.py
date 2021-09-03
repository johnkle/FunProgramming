#排序后目标值左边的值等于索引i+1,右边的值小于索引i+1，从两边向中间逼近
class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        left = 0
        right = len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            if nums[mid] < mid+1:
                #收缩右边界
                right = mid
            else:
                #收缩左边界
                left = mid+1
        return nums[left]


class Solution2:
    def findDuplicate(self, nums):
        lookup = set()
        for x in nums:
            if x in lookup:
                return x
            lookup.add(x)
        return 