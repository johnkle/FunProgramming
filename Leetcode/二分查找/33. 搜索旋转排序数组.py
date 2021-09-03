# 在常规二分搜索的时候查看当前 mid 为分割位置分割出来的两个部分 [l, mid] 和 [mid + 1, r] 哪个部分是有序的，
# 并根据有序的那个部分确定我们该如何改变二分搜索的上下界，因为我们能够根据有序的那部分判断出 target 在不在这个部分：

# 如果 [l, mid - 1] 是有序数组，且 target 的大小满足 [nums[l],nums[mid])，
# 则将搜索范围缩小至 [l, mid - 1]，否则在 [mid + 1, r] 中寻找。
# 如果 [mid, r] 是有序数组，且 target 的大小满足 (nums[mid+1],nums[r]]，
# 则将搜索范围缩小至 [mid + 1, r]，否则在 [l, mid - 1] 中寻找。

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left]<=target and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<target and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
        
class Solution(object):
    def search(self, nums, target):
        return -1 if target not in nums else nums.index(target)