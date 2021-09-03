class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n>0:
            t = self.myPow(x,n//2)
            if n%2:
                return x*t*t
            else:
                return t*t
        else:
            t = self.myPow(x,-n//2)
            if -n%2:
                return 1/(x*t*t)
            else:
                return 1/(t*t)