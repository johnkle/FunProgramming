# 如何使用常数空间复杂度
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        p = dummy
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst.sort()
        for x in lst:
            p.next = ListNode(x)
            p = p.next
        return dummy.next

#先找中点，再归并
class Solution(object):
    def sortList(self, head):
        def sortfunc(head):
            if not head or not head.next:
                return head
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return merge(sortfunc(head),sortfunc(mid))
        def merge(node1,node2):
            if not node1:
                return node2
            elif not node2:
                return node1
            elif node1.val < node2.val:
                node1.next = merge(node1.next,node2)
                return node1
            else:
                node2.next = merge(node1,node2.next)
                return node2
        return sortfunc(head)
