# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next
        while stack:
            if head.val != stack.pop():
                return False
            head = head.next
        return True

class Solution2(object):
    def isPalindrome(self, head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        left = 0
        right = len(lst)-1
        while left <= right:
            if lst[left] !=lst[right]:
                return False
            left += 1
            right -= 1
        return True

class Solution3(object):
    def isPalindrome(self, head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        left = 0
        right = len(lst)-1
        return lst == lst[::-1]