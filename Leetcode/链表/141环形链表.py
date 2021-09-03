class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        lookup = dict()
        index = 0
        while head:
            if head in lookup:
                return True
            lookup[head] = index
            index += 1
            head = head.next
        return False

#一次遍历
class Solution2(object):
    def hasCycle(self, head):
        if not head:
            return False
        lookup = set()
        while head:
            if head in lookup:
                return True
            lookup.add(head)
            head = head.next
        return False    

#快慢指针
class Solution3:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

class Solution4:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False