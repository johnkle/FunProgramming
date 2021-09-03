#如何用O(1)空间复杂度
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        if not head:
            return head
        lst = []
        while head:
            lst.append(head)
            head = head.next
        left = 0
        right = len(lst)-1
        while left < right:
            lst[left].next = lst[right]
            lst[right].next =lst[left+1]
            left += 1
            right -= 1
        #最后指向空，否则有环
        lst[left].next = None
        return head

class Solution2(object):
    def reorderList(self, head):
        if not head:
            return head
        dummy = ListNode(0)
        p = dummy
        lst = []
        nodes = []
        while head:
            lst.append(head)
            head = head.next
        left = 0
        right = len(lst)-1
        while left <= right:
            if left == right:
                nodes.append(lst[left])
                break
            nodes.append(lst[left])
            nodes.append(lst[right])
            left += 1
            right -= 1
        for node in nodes:
            p.next = node
            p = p.next
        p.next = None
        return dummy.next

            
        