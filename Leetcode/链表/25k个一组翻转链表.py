class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        def reverse(head):
            if not head or not head.next:
                return head
            newhead = reverse(head.next)
            head.next.next = head
            head.next = None
            return newhead
        tail = head
        for _ in range(1,k):
            if not tail:
                return head
            tail = tail.next
        if not tail:
            return head
        after = tail.next
        tail.next = None
        newhead = reverse(head)
        head.next = self.reverseKGroup(after,k)
        return newhead