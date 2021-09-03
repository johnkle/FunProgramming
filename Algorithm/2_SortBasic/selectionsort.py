def selectionSort(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[j] < L[i]:
                L[i],L[j] = L[j],L[i]
    

L1 = [1,3,5,6,4,2]
L2 = ['b','a','d','c','f','e']
selectionSort(L1)
selectionSort(L2)
print(L1,L2)




