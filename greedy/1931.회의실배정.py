n = int(input())
arr = []
start ,end = 0,0
cnt = 0
res = 0
target= 0
save = 0
for a in range(n):
    data1,data2 = map(int,input().split())
    arr.append((data1,data2))

arr.sort()
#arr = sorted(arr,key=lambda x: abs(x[0]-x[1]))
arr = sorted(arr,key= lambda x: x[1])
print(arr)
for a in arr:
    if a[0] >= start:
        start = a[1]
        cnt += 1
    
def binary_search(arr,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid][0] == target:
        return mid
    elif arr[mid][0] < target:
        return binary_search(arr,target,mid+1,end)
    else:
        return binary_search(arr,target,start,mid-1)
        
    start = arr[0][0]
    end = arr[0][1]
    cnt += 1
#while True:
#    save = binary_search(arr,end,0,n-1)
#    if save == None:
#        end += 1
#    else:
#        start = arr[binary_search(arr,end,0,n-1)][0]
#        end = arr[binary_search(arr,end,0,n-1)][1]
#        print(start,end)
#        cnt += 1
    
#    if end == arr[n-1][1]:
#        break
print(cnt)


