#相当于多叉树的深度优先搜索
class Solution:
    def isUgly(self, n: int) -> bool:
        #终止条件
        if n==0:
            return False
        if n==1:
            return True
        if n%2!=0 and n%3!=0 and n%5!=0:
            return False
        #递归，深度优先搜索
        if n%2==0:
            return self.isUgly(n//2)
        if n%3==0:
            return self.isUgly(n//3)
        if n%5==0:
            return self.isUgly(n//5)
        return self.isUgly(n)