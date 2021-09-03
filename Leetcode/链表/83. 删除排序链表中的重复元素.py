class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        p = self.deleteDuplicates(head.next)
        if head.val != p.val:
            head.next = p
            return head
        return p