# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        if not head or not head.next:
            return head
        slow = fast = head
        length = 1
        while fast.next:
            fast = fast.next
            length += 1
        step = length-k
        while step:
            slow = slow.next
            step -= 1
        return slow
#一次遍历
class Solution(object):
    def getKthFromEnd(self, head, k):
        slow = fast = head
        while k>0:
            if not fast:
                return
            fast = fast.next
            k -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow