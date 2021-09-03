class Solution:
    def productExceptSelf(self, nums):
        L = [0]*len(nums)
        R = [0]*len(nums)
        L[0] = 1
        R[-1] = 1
        output = [0]*len(nums)
        for i in range(1,len(nums)):
            L[i] = L[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            R[j] = R[j+1]*nums[j+1]
        for i in range(len(nums)):
            output[i] = L[i]*R[i]
        return output