class Solution():
    #如何原地排序
    def mergeSort(self,nums,left,right):
        if not nums:
            return
        if left > right:
            return
        if left == right:
            return [nums[left]]
        mid = left + (right-left)//2
        numsl = self.mergeSort(nums,left,mid)
        numsr = self.mergeSort(nums,mid+1,right)
        return self.merge(numsl,numsr)
    #如何原地归并
    def merge(self,nums1,nums2):
        if not nums1:
            return nums2
        elif not nums2:
            return nums1
        elif nums1[0] < nums2[0]:
            return [nums1[0]] + self.merge(nums1[1:],nums2)
        else:
            return [nums2[0]] + self.merge(nums1,nums2[1:])

if __name__ == "__main__":
    sl = Solution()
    arr = [1,3,5,7,2,4,6,19,15]
    print(sl.mergeSort(arr,0,len(arr)-1))
    print(sl.merge([1,3,5],[2,4,6]))