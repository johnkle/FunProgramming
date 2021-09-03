class Solution(object):
    def shuffle(self, nums, n):
        res = [0]*2*n
        for i in range(n):
            res[i*2] = nums[i]
            res[i*2+1] = nums[n+i]
        return res

class Solution(object):
    def shuffle(self, nums, n):
        res = []
        left = 0
        right = n
        while left < n:
            res.append(nums[left])
            res.append(nums[right])
            left += 1
            right += 1
        return res