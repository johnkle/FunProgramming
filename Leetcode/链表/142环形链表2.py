# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        hashmap = dict()
        i = 0
        while head:
            if head in hashmap:
                return head
            hashmap[head] = i
            head = head.next
            i += 1
        return None