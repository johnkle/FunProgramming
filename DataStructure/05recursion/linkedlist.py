from node import Node
class ListNode():
    def __init__(self):
        self.head=None
        self.dummy=Node(-1)
        self.dummy.next=self.head
        self.prev=self.dummy
        self.size=0   
    #遍历
    def traverse(self):
        self.cur = self.head
        L=[]
        while self.cur!=None:
            L.append(self.cur.data)
            self.cur = self.cur.next
        print(L)
    #增，找到待插入索引的前一个位置
    def insert(self,index,e):
        self.prev.next = self.head
        for _ in range(0,index):
            self.prev=self.prev.next
        # Node(e).next=self.prev.next
        # self.prev.next=Node(e)
        self.prev.next=Node(e,self.prev.next)
        self.size+=1
    #删1,找到待删除索引的前一个位置
    def delindex(self,index):
        self.prev.next = self.head
        for _ in range(0,index):
            self.prev=self.prev.next
        self.prev.next=self.prev.next.next
    #删2
    def dele(self,e):
        self.prev.next = self.head
        while self.prev.next!=None:
            if self.prev.next.data==e:
                self.prev.next=self.prev.next.next
                self.size-=1
            self.prev=self.prev.next
    #删3
    def delrecur(self,head,e):
        if head==None:
            return head
        self.res=self.delrecur(head.next,e)
        if head.data==e:
            return self.res
        else:
            head.next=self.res
            return head
    #改
    def revise(self,a,b):
        self.cur = self.head
        while self.cur != None:
            if self.cur.data == a:
                self.cur.data = b
            self.cur = self.cur.next
    
    #查
    def find(self,e):
        self.cur = self.head
        self.index = 0
        while self.cur != None:
            if self.cur.data == e:
                return self.index
            self.cur = self.cur.next
            self.index+=1

    def arrlist(self,arr):
        self.head=Node(arr[0])
        self.cur = self.head
        for i in range(1,len(arr)):
            # 向右添加
            self.cur.next = Node(arr[i])
            self.cur = self.cur.next
        # for i in range(0,len(arr)):
        #     self.cur = Node(arr[i])
        #     self.cur = self.cur.next
            #向左添加
            # self.cur = Node(arr[i],self.cur)
    def test(self):
        self.L = []
        self.cur=self.head
        while self.cur != None:
            self.L.append(self.cur.data)
            self.cur = self.cur.next
        print(self.L)

S = [1,2,9,3,4,5,6]
listnode = ListNode()
listnode.arrlist(S)
# listnode.revise(9,11)
# listnode.delindex(3)
# listnode.dele(6)
# listnode.traverse()
# k=listnode.find(6)
# listnode.insert(2,12)
listnode.delindex(2)
# print(k)
listnode.test()


# listnode.insert(5,12)
# print(listnode.head.next.next.data)
# print(listnode.dummy.next.data)