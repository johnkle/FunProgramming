class Solution:
    def mySqrt(self, x):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x and (mid+1)*(mid+1) > x:
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return ans

class Solution2:
    def mySqrt(self, x):
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans