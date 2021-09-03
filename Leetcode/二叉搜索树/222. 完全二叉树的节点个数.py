class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        return self.countNodes(root.left)+self.countNodes(root.right)+1

class Solution2(object):
    def countNodes(self, root):
        if not root:
            return 0
        res = []
        queue = [root]
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return len(res)