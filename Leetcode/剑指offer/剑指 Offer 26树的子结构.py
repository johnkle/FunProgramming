# 求解思路可以分解为以下两步：
# 匹配根节点：首先在 A 中找到与 B 的根节点匹配的节点 node；
# 匹配其他节点：验证 node 的子树与 B 的子树是否匹配。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        if not A or not B:
            return False
        return self.doesAHaveB(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)
    def doesAHaveB(self,A,B):
        #验证以A为根节点的子树是否包含和B一样的结构
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.doesAHaveB(A.left,B.left) and self.doesAHaveB(A.right,B.right)

#寻找A中节点值和B相同的节点，找到后check，check失败再从左右子树寻找
class Solution2(object):
    def isSubStructure(self, A, B):
        if not A or not B:
            return False
        res = False
        if A.val == B.val:
            res = self.doesAHaveB(A,B)
        if not res:
            res = self.isSubStructure(A.left,B)
        if not res:
            res = self.isSubStructure(A.right,B)
        return res
    def doesAHaveB(self,A,B):
        if not B:
            return True
        if not A:
            return False
        if A.val != B.val:
            return False
        return self.doesAHaveB(A.left,B.left) and self.doesAHaveB(A.right,B.right)