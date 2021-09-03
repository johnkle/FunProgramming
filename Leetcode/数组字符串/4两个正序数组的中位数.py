class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1+nums2
        nums.sort()
        if len(nums)%2 == 1:
            mid = len(nums)//2
            return nums[mid]
        else:
            mid = len(nums)//2
            return (nums[mid-1]+nums[mid])/2

sl = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(sl.findMedianSortedArrays(nums1,nums2))
