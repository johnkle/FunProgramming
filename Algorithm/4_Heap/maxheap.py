#最大堆是一个完全二叉树，父亲节点大于孩子节点的值
# parent=k 
# leftchild = 2*k 
# rightchild = 2*k+1

import random

class MaxHeap():
    def __init__(self):
        self.data = [0]
        self.count = 0
    
    #传入arr,构造最大堆
    def maxheap(self,arr,n):
        for i in range(0,n):
            self.data.append(arr[i]) #不能self.data[i+1]=arr[i]
        self.count = n
        for i in range(self.count//2,0,-1): #从第一个非叶子节点shiftdown
            self.shiftdown(i)

    def shiftup(self,k):
        #从k=2开始比较，1节点无需shiftup
        while k>1 and (self.data[k] > self.data[k//2]):
            self.data[k],self.data[k//2] = self.data[k//2],self.data[k]
            k//=2
    
    def shiftdown(self,k):
        while 2*k<=self.count:#如果有左孩子则执行循环,'='别少
            j = 2*k #体会j的含义
            if j+1<=self.count and self.data[j+1]>self.data[j]:
                j+=1
            if self.data[k]>=self.data[j]:
                break
            self.data[j],self.data[k] = self.data[k],self.data[j]
            k = j
            
    def insert(self,e):
        #self.data[self.count+1] = e 空数组不能这样操作
        self.data.append(e)
        self.count+=1
        self.shiftup(self.count)
    
    def extractmax(self):
        assert(self.count>0)
        self.ret = self.data[1]
        self.data[1],self.data[self.count] = self.data[self.count],self.data[1]
        self.count-=1
        self.shiftdown(1)
        return self.ret
    
    def size(self):
        return self.count
        
    def isEmpty(self):
        return self.count == 0

#test
maxheap = MaxHeap()
for i in range(1,12):
    maxheap.insert(random.randint(1,20))
print(maxheap.data)

# print(maxheap.extractmax())
# print(maxheap.data[11])#注意extractmax之后count-1,data[11]访问不到

# maxheap = MaxHeap()
# a=maxheap.size()
# print(a)
# b=maxheap.isEmpty()
# print(b)