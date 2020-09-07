N = int(input())
arr = list(map(int,input().split()))

save = [0 for _ in range(N)]

save[0] = arr[0]
save[1] = max(arr[0],arr[1])
for a in range(2,N):
    save[a] = max(save[a-1],arr[a]+save[a-2])

print(save)