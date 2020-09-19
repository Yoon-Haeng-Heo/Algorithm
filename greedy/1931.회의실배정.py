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
#print(arr)
for a in arr:
    if a[0] >= start:
        start = a[1]
        cnt += 1
    
print(cnt)


