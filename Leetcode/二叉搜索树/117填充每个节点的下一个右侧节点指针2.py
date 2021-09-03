# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        if not root:
            return root
        queue = [root]
        while queue:
            dummy = Node()
            for i in range(len(queue)):
                node = queue.pop(0)
                if i!=0:
                    dummy.next = node
                dummy = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
