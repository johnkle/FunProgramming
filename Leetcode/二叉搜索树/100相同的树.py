class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p:
            return not q
        if not q:
            return not p
        return p.val==q.val and self.isSameTree(p.left,q.left)\
            and self.isSameTree(p.right,q.right)