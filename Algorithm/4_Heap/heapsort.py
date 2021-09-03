from maxheap import MaxHeap
maxheap1 = MaxHeap()
def heapsort1(arr,n):
    for i in range(0,n):
        maxheap1.insert(arr[i])
    for i in range(n-1,-1,-1):
        arr[i] = maxheap1.extractmax()

arr = [3,1,6,2,9,7]
heapsort1(arr,6)
print(arr)
print(maxheap1.data)
# #每次实例化都执行__init__,所以返回空
# size = maxheap1.size()
# print(size)
# isEmpty = maxheap1.isEmpty()
# print(isEmpty)
# a=maxheap1.extractmax()
# print(a)
# for i in range(5,-1,-1):
#     arr[i] = maxheap1.extractmax()
# a=maxheap1.extractmax()

# maxheap2 = MaxHeap()
# def heapsort2(arr,n):
#     maxheap2.maxheap(arr,n)
#     for i in range(n-1,-1,-1):
#         arr[i] = maxheap2.extractmax()

# arr = [3,1,6,2,9,7]
# heapsort2(arr,6)
# print(arr)
# print(maxheap2.data)



