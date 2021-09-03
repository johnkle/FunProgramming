class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        res = []
        i =0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i == m:
            res.extend(nums2[j:])
        if j == n:
            res.extend(nums1[i:])
        return res

class Solution2(object):
    def merge(self, nums1, nums2):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        if nums1[0] < nums2[0]:
            return [nums1[0]]+self.merge(nums1[1:],nums2)
        else:
            return [nums2[0]]+self.merge(nums1,nums2[1:])





if __name__ == "__main__":
    sl = Solution2()
    nums1 = [1,2,3]
    nums2 = [4,5,6]
    #print(sl.merge(nums1,3,nums2,3))
    print(sl.merge(nums1,nums2))