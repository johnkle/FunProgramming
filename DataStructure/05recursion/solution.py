from node import Node
#找到待删除节点的前一个节点,把next指向下一个节点，维护指针
class Solution():
    def removevalue(self,head,value):
        self.dummyhead = Node(-1)
        self.dummyhead.next = head
        self.prv = self.dummyhead
        while self.prv.next != None:
            if self.prv.next.data == value:
                self.prv.next = self.prv.next.next
            else:
                self.prv = self.prv.next

