# 先连接成环，再旋转
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        slow = fast = cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        i = k%length
        if i == 0:
            return head
        while fast.next:
            if i > 0:
                fast = fast.next
                i -= 1
            else:
                slow = slow.next
                fast = fast.next
        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead

class Solution2(object):
    def rotateRight(self, head, k):
        if not head:
            return
        slow = head
        fast = head
        length = 1
        while fast.next:
            length += 1
            fast = fast.next
        fast.next = head
        step = length - k%length-1
        while step > 0:
            slow = slow.next
            step -= 1
        newHead = slow.next
        slow.next = None
        return newHead


class Solution3(object):
    def rotateRight(self, head, k):
        temp = []
        while head:
            temp.append(head)
            head = head.next
        for _ in range(k):
            prev = temp.pop(-1)
            temp.insert(0,prev)
        dummyHead = ListNode(0)
        cur = dummyHead
        for node in temp:
            cur.next = node
            cur = cur.next
        return dummyHead.next
