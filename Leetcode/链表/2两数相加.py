# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = ListNode(int(num[0]))
        cur = head
        for i in range(1,len(num)):
            cur.next = ListNode(int(num[i]))
            cur = cur.next
        return head