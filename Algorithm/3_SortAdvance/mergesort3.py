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
        temp = nums[l:r+1]
        i = l
        j = mid +1
        for k in range(l,r+1):
            # while i < mid+1 and j < r+1:
            #     if temp[i-l]<temp[j-l]:
            #         nums[k] = temp[i-l]
            #         i += 1
            #     else:
            #         nums[k] = temp[j-l]
            #         j += 1
            if i > mid:
                nums[k] = temp[j-l]
                j += 1
            elif j > r:
                nums[k] = temp[i-l]
                i += 1
            elif temp[i-l]<temp[j-l]:
                nums[k] = temp[i-l]
                i += 1
            else:
                nums[k] = temp[j-l]
                j += 1

if __name__ == "__main__":
    sl3 = Solution()
    nums = [5,3,1,7,2,22,6,19,15,18]
    print(sl3.mergesort(nums,0,len(nums)-1))
