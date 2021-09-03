#中位数作为根节点的值，再递归构造左右子树
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        lst = []
        while head:
            list.append(head.val)
            head = head.next
        def helper(lst,left,right):
            if left > right:
                return
            mid = left + (right-left)//2
            root = TreeNode(lst[mid])
            root.left = helper(lst,left,mid-1)
            root.right = helper(lst,mid+1,right)
            return root
        return helper(lst,0,len(lst)-1)

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        return buildTree(head, None)