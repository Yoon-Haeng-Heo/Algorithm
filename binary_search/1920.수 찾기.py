n = int(input())
narr = list(map(int,input().split()))
m = int(input())
marr = list(map(int,input().split()))

def binary_search(arr,target,start,end):
    if start > end:
        return None
    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)

narr.sort()
res = 0
for a in marr:
    res = binary_search(narr,a,0,n-1)
    if res != None:
        print(1)
    else:
        print(0)