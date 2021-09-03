class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # if not nums:
        #     return []
        # if len(nums) == 1:
        #     return [str(nums[0])]
        res = []
        left = 0
        right = 0
        while right < len(nums):
            if right < len(nums)-1 and nums[right+1]-nums[right] == 1:
                right += 1
            else:
                if left == right:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left])+'->'+str(nums[right]))
                right += 1
                left = right
        return res