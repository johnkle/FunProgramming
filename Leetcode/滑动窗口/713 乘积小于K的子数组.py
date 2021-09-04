class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        left = 0
        right = 0
        window = 1
        res = 0
        while right < len(nums):
            window *= nums[right]
            while window >= k:
                window /= nums[left]
                left += 1
            #以right结尾的乘积小于k的子数组的数目
            res += right-left+1
            right += 1
        return res