class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return
        newhead = self.removeElements(head.next,val)
        if head.val != val:
            head.next = newhead
            return head
        return newhead