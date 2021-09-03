def insertSort(L,n):
    for i in range(1,n):
        for j in range(i,0,-1):
            if L[j] < L[j-1]:
                L[j],L[j-1] = L[j-1],L[j]
            else:
                continue

L = [2,1,4,6,5,3,0]
L2 = ['b','a','d','c','f','e']
insertSort(L,7)
insertSort(L2,6)
print(L,L2)

# def sort1(L,n):
#     for i in range(n-1,0,-1):
#         if L[i] < L[i-1]:
#             L[i],L[i-1] = L[i-1],L[i]

# L=[2,3,5,1,6,4]
# sort1(L,6)
# print(L)




