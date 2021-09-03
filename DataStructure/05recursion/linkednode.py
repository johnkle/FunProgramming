from node import Node
class ArrNode():
    def __init__(self,head):
        self.head = None
    
    def ArrNode(self):
        for count in range(1,6):
            #self.head = Node(count,self.head)
            node = Node(count)
            node.next = self.head
            self.head = node
    def test(self):
        L = []
        while self.head != None:
            # print(self.head.data)
            # self.head = self.head.next
            L.append(self.head.data)
            self.head = self.head.next
        print(L)


arrnode = ArrNode(None)
arrnode.ArrNode()
arrnode.test()