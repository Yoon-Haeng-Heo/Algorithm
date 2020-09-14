n = int(input())

arr = []
for a in range(n):
    arr.append(int(input()))
arr = sorted(arr,reverse = True)

for a in arr:
    print(a,end = ' ')