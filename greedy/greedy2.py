n,m = map(int,input().split())

res = 0 
cnt = 0

for a in range(n):
    arr = list(map(int,input().split()))
    val = min(arr)
    res = max(val,res)
print(res)