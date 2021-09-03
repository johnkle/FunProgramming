class Solution():

    def mergesort(self,nums,l,r):
        if l >= r:
            return
        mid = (l+r)//2
        self.mergesort(nums,l,mid)
        self.mergesort(nums,mid+1,r)
        self.merge(nums,l,mid,r)
        return nums

    #将nums[l...mid]和nums[mid+1...r]两部分进行归并
    def merge(self,nums,l,mid,r):
        #需要一个辅助数组
        temp = nums[l:r+1]
        i = l
        j = mid +1
        k = l
        while i < mid+1 and j < r+1:
            if temp[i-l] < temp[j-l]:
                nums[i] = temp[i-l]
                i += 1
    
            else:
                nums[j] = temp[j-l]
                j += 1
            k += 1
        if i>mid:
            nums[k+1:r+1] = temp[j-l:]
        if j>r:
            nums[k+1:r+1] = temp[i-l:mid+1]

if __name__ == "__main__":
    sl3 = Solution()
    arr = [1,3,5,7,2,4,6,19,15]
    #sl3.merge(arr,0,(len(arr)-1)//2,len(arr)-1)
    print(sl3.mergesort(arr,0,len(arr)-1))
