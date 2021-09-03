# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         nums = nums1+nums2
#         nums.sort()
#         if len(nums)%2 == 1:
#             mid = len(nums)//2
#             return nums[mid]
#         else:
#             mid = int(len(nums)//2)
#             return (nums[mid-1]+nums[mid])/2

# sl = Solution()
# nums1 = [1,2]
# nums2 = [3,4]
# print(sl.findMedianSortedArrays(nums1,nums2))


def combinationSum(candidates,target):
    if not candidates or target < 0:
        return []
    res = []
    def dfs(candidates,idx,path):
        if sum(path) == target:
            res.append(path.copy())
            return
        if sum(path) > target:
            return
        for i in range(idx,len(candidates)):
            if i>idx and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            dfs(candidates,i,path)
            path.pop()
    candidates.sort()
    dfs(candidates,0,[])
    return res

candidates = [2,2,2,3,6,7]
target = 7
print(combinationSum(candidates,target))