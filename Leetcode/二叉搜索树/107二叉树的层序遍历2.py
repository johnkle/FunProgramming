import collections
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        deque = collections.deque([root])
        res = []
        while deque:
            temp = []
            for _ in range(len(deque)):
                node = deque.popleft()
                temp.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(temp)
        return list(reversed(res))