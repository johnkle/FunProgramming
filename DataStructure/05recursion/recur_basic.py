def sum(arr):
    return sum1(arr,0,len(arr)-1)
def sum1(arr,l,r):
    # if l > r:
    #     return 0
    if l==r:
        return arr[r]
    L = arr[l]+sum1(arr,l+1,r)
    return L

arr = [1,2,3,4,5,6]
print(sum(arr))