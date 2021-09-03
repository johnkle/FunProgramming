class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def divider(nums,left,right):
            if left == right:
                return nums[left]
            mid = left + (right-left)//2
            majorleft = divider(nums,left,mid)
            majorright = divider(nums,mid+1,right)
            if majorleft == majorright:
                return majorleft
            countleft = nums[left:right+1].count(majorleft)
            countright = nums[left:right+1].count(majorright)
            return majorleft if countleft>countright else majorright
        return divider(nums,0,len(nums)-1)