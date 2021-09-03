class Solution(object):
    def mergeKLists(self, nums,left,right):
        if not nums:
            return
        if left == right:
            return nums[left]
        mid = left + (right-left)//2
        numsl = self.mergeKLists(nums,left,mid)
        numsr = self.mergeKLists(nums,mid+1,right)
        return self.mergeTwoLists(numsl,numsr)

    def mergeTwoLists(self,nums1,nums2):
        if not nums1:
            return nums2
        elif not nums2:
            return nums1
        elif nums1[0] < nums2[0]:
            return [nums1[0]] + self.mergeTwoLists(nums1[1:],nums2)
        else:
            return [nums2[0]] + self.mergeTwoLists(nums1,nums2[1:])

if __name__ == "__main__":
    sl = Solution()
    nums = [[1,4,5],[1,3,4],[2,6],[2,6,7]]
    print(sl.mergeKLists(nums,0,len(nums)-1))
