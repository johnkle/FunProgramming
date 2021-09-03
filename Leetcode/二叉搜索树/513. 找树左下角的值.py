import collections
class Solution:
    def findBottomLeftValue(self, root):
        def bfs(root):
            if not root:
                return
            res = []
            queue = collections.deque([root])
            while queue:
                res = queue[0].val
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return res
        return bfs(root)