n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

start = arr[0]
end = arr[len(arr)-1]
mid = (start+end) // 2

res = 0
while (start <= end):
    
    total = 0
    mid = (start+end)//2
    for a in arr:
        if a > mid:
            total += (a - mid)
    if total < m:
        end = mid -1
    else :
        res = mid
        start = mid + 1
print(res)