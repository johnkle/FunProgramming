class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        slow = fast = dummy = ListNode(0)
        dummy.next = head
        i = 0
        while fast.next:
            if i < n:
                fast = fast.next
                i += 1
            else:
                slow = slow.next
                fast = fast.next
        slow.next = slow.next.next
        return dummy.next