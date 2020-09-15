k,n = map(int,input().split())
data = []
for a in range(k):
    data.append(int(input()))

start = 0 
end = max(data)
res = 0

def check(arr,target):
    #lensum = 0
    cnt = 0
    for a in arr:
        #lensum += (target * (a // target))
        cnt += (a // target)
    return cnt

while (start <= end):
    mid = (start + end) // 2
    if mid == 0:
        res = 1
        break
    elif check(data,mid) >= n:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)
    

