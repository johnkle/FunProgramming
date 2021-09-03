def dele(self,head,e):
    if head==None:
        return head
    head.next=self.dele(head.next,e)