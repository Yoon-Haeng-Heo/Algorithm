n = int(input())
arr = []
for a in range(n):
    data = input().split()
    arr.append((data[0],data[1]))

arr = sorted(arr,key = lambda x: x[1])
for a in arr:
    print(a[0],end = ' ')