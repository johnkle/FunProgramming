# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return
        prev = None
        cur = head
        while cur:
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        return prev

class Solution2(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

class Solution3(object):
    def reverseList(self, head):
        if not head:
            return
        stack = []
        while head:
            stack.append(head)
            head = head.next
        dummyHead = ListNode(0)
        cur = dummyHead
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        return dummyHead