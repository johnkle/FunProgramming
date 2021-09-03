# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        self.drivenode = None
        def reverseN(head,n):
            if n == 1:
                self.drivenode = head.next
                return head
            newhead = reverseN(head.next,n-1)
            head.next.next = head
            head.next = self.drivenode
            return newhead
        if m == 1:
            return reverseN(head,n)
        head.next = self.reverseBetween(head.next,m-1,n-1)
        return head