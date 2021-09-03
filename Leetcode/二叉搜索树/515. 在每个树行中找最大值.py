import collections
class Solution:
    def largestValues(self, root):
        if not root:
            return []
        res = []
        deque = collections.deque([root])
        while deque:
            cur = float('-inf')
            for i in range(len(deque)):
                node = deque.popleft()
                cur = max(cur,node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(cur)
        return res