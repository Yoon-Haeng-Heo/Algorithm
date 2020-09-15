n,m = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
end = max(arr)
res = 0

while (start <= end):
    mid = (start + end) // 2
    total = 0
    for a in arr:
        if a > mid:
            total += (a - mid)
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid+1
print(res)