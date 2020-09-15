def binary_search(arr,target,start,end):
    if start > end:
        return None
    mid = (start + end)//2
    if target == arr[mid]:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
sarr = list(map(int,input().split()))

arr.sort()
for a in sarr:
    res = binary_search(arr,a,0,n-1)
    if res != None:
        print('yes')
    else:
        print('no')
