#最大堆是一个完全二叉树
#parent=(k-1)//2
#leftchild = 2*k+1
#rightchild = 2*k+2
#最后一个非叶子节点索引(count-1)/2

#原地堆排序
def shiftdown(arr,n,k):
        while 2*k+1<n:#如果有左孩子则执行循环,'='别少
            j = 2*k+1 #体会j的含义
            if j+1<n and arr[j+1]>arr[j]:
                j+=1
            if arr[k]>=arr[j]:
                break
            arr[j],arr[k] = arr[k],arr[j]
            k = j

def heapsort2(arr,n):
    for i in range ((n-1)//2,-1,-1): #给定arr构造最大堆
        shiftdown(arr,n,i)
    # for i in range(0,n-1):
    #     arr[0],arr[n-1-i] = arr[n-1-i],arr[0]
    #     shiftdown(arr,n-1-i,0)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        shiftdown(arr,i,0)

L = [3,1,6,2,9,7,0]
heapsort2(L,7)
print(L)