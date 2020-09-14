n,k = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort()
arr2 = sorted(arr2,reverse=True)
for a in range(k):
    if arr1[a] < arr2[a]:
        arr1[a] , arr2[a] = arr2[a], arr1[a]
    else : break
print(sum(arr1))

