def merge(arr,lo,mid,hi):
    i = lo
    j = mid+1
    aux=[]
    aux = arr[lo:hi+1]
    for k in range(lo,hi+1):
        if i>mid:
            arr[k] = aux[j-lo]
            j+=1
        elif j>hi:
            arr[k] = aux[i-lo]
            i+=1
        elif aux[j-lo]<aux[i-lo]:
            arr[k] = aux[j-lo]
            j+=1
        else:
            arr[k] = aux[i-lo]
            i+=1

def mergeSort(arr,lo,hi):
    if hi <= lo:
        return
    mid = int((lo+hi)/2)
    mergeSort(arr,lo,mid)
    mergeSort(arr,mid+1,hi)
    merge(arr,lo,mid,hi)
    return arr

L=arr = [5,3,1,7,2,22,6,19,15,18]
print(mergeSort(L,0,len(arr)-1))