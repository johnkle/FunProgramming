# 对于有序数组才能使用二分查找
# def binarysearch1(arr,e):
#     l = 0
#     r = len(arr)-1
#     while l <= r:
#         mid = int((l+r)/2)
#         if arr[mid] == e:
#             return mid
#         if arr[mid]>e:
#             r = mid-1
#         else:
#             l = mid+1
#     return -1

# L = [3,1,6,2,9,7]
# target=binarysearch1(L,2)
# print(target)


# def binarysearch2(arr,l,r,e):
#     mid = int((l+r)/2)
#     if arr[mid]==e:
#         return mid
#     if arr[mid]>e:
#         r = mid-1
#         return binarysearch2(arr,l,r,e)
#     else:
#         l = mid+1
#         return binarysearch2(arr,l,r,e)


def binarySearch3(arr,val):
    left = 0
    right = len(arr)
    while left<=right:
        mid = left+(right-left)//2
        if arr[mid]==val:
            return mid
        if arr[mid]<val:
            left = mid+1
        if arr[mid]>val:
            right = mid-1
    return False


L = [1,2,3,6,7,9,11,15,17,18,21]
target=binarySearch3(L,18)
print(target)




# def binarySearch(arr,val):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=left+(right-left)//2
#         if arr[mid] == val:
#             return mid
#         if arr[mid]<val:
#             right=mid-1
#         else:
#             left=mid+1
#     return False



# L = [3,1,6,2,9,7,11]
# target=binarySearch(L,2)
# print(target)