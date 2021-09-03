#最大堆是一个完全二叉树，父亲节点大于孩子节点的值
# 节点k(k从0开始)
# 父节点(k-1)//2
# leftchild = 2*k+1 
# rightchild = 2*k+2
import random
class MaxHeap():
    def __init__(self):
        self.data = []
        self.count = 0
    
    #从第k个节点shiftUp,一直到count位置
    def shiftUp(self,k):
        # while k > 1:
        #     if self.data[k] > self.data[k//2]:
        #         self.data[k],self.data[k//2]=self.data[k//2],self.data[k]
        #     k = k//2
        # while k > 1 and self.data[k] > self.data[k//2]:
        #     self.data[k],self.data[k//2]=self.data[k//2],self.data[k]
        #     k = k//2
        while k > 0 and self.data[k] > self.data[(k-1)//2]:
            self.data[k],self.data[(k-1)//2]=self.data[(k-1)//2],self.data[k]
            k = (k-1)//2


    
    #从第k个节点shiftDown,一直到count位置
    def shiftDown(self,k):
        #如果有左孩子则执行循环
        while 2*k+1 <= self.count:
            #j指向左右孩子最大值索引
            #指向左孩子
            j = 2*k+1
            #若存在右孩子且右孩子大于左孩子，则指向右孩子
            if 2*k+2<=self.count and self.data[2*k+2]>self.data[2*k+1]:
                j = j+1
            #若不小于左右孩子最大值，跳出循环
            if self.data[k] >= self.data[j]:
                break
            #否则交换
            self.data[k],self.data[j]=self.data[j],self.data[k]
            #更新索引
            k = j
    
    #从末尾向堆中添加元素
    def addLast(self,e):
        self.data.append(e)
        #更新最后一个元素的索引
        self.count += 1
        self.shiftUp(len(self.data)-1)
        #注意是count-1
        #self.shiftUp(self.count-1)
    
    #取出堆中最大元素
    def extractMax(self):
        ret = self.data[0]
        self.data[0],self.data[self.count]=self.data[self.count],self.data[0]
        self.count-=1
        self.shiftDown(0)
        return ret
        
    #取出堆中最大元素，并替换成元素e
    def replace(self,e):
        ret = self.data[0]
        self.data[0] = e
        self.shiftDown(0)
        return ret
    
    #将任意数组整理成堆的形式
    def heapify(self,arr):
        self.data = arr
        self.count = len(arr)-1
        #从最后一个非叶子节点shiftDown
        for i in range((len(arr)-2)//2,-1,-1):
            self.shiftDown(i)


if __name__ == "__main__":
    #测试heapify
    testArr = []
    testData = [2,1,6,11,8,12,30,18,22,25,15]
    maxheap = MaxHeap()
    maxheap.heapify(testData)
    print(maxheap.data)
    #堆排序
    for i in range(len(testData)):
        testArr.insert(0,maxheap.extractMax())
    print(testArr)

    #测试addLast
    # maxheap = MaxHeap()
    # for i in range(12):
    #     maxheap.addLast(random.randint(1,20))
    # print(maxheap.data)


        