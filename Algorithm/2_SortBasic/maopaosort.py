#n-1次排序，每一次排序都对剩下的n-1-i个元素进行遍历交换
#每一次排序从n-1开始
def maopaoSort(L1,n):
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if L1[j] < L1[j-1]:
                L1[j],L1[j-1] = L1[j-1],L1[j]

L1 = [2,1,4,6,3,5,0,]
maopaoSort(L1,7)
print(L1)

#每一次排序从0开始
def maopao(L2,n):
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if L2[j]>L2[j+1]:
                L2[j],L2[j+1]=L2[j+1],L2[j]

L2 = [2,1,4,6,3,5,0]
maopao(L2,7)
print(L2)