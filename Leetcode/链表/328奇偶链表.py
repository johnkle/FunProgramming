# 参考86分隔链表
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        before = beforehead = ListNode(0)
        after = afterhead = ListNode(0)
        index = 1
        while head:
            if index%2 == 1:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
            index += 1
        after.next = None
        before.next = afterhead.next
        return beforehead.next


class Solution:
    def oddEvenList(self, head):
        odd = oddhead = ListNode(0)
        even = evenhead = ListNode(0)
        cur = head
        i = 1
        while cur:
            if i%2:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
            i += 1
        even.next = None
        odd.next = evenhead.next
        return oddhead.next