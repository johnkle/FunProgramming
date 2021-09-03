
def merge(arr,l,mid,r):
    arr_copy=[]
    # for i in range(l,r+1):
    #     arr_copy[i-l] = arr[i]
    for i in range (l,r+1):
        arr_copy.append(arr[i])
    
    i = l
    j=mid+1

    for k in range(l,r+1):
        if i>mid:
            arr[k] = arr_copy[j-l]
            j+=1
        elif j>r:
            arr[k] = arr_copy[i-l]
        elif arr_copy[i-l] < arr_copy[j-l]:
            arr[k] = arr_copy[i-l]
            i+=1
        else:
            arr[k] = arr_copy[j-l]
            j+=1

def mergeSort(arr,l,r):
    if l == r:
        return arr[r]
    mid = int((l+r)//2)
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)

L=[2,5,1,3,7,9]
mergeSort(L,0,5)
print(L)