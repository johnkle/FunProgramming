class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        if not root:
            return
        res = []
        queue = [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.children:
                    queue.extend(cur.children)
            res.append(temp)
        return res