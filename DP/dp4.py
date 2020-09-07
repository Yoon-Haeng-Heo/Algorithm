n, m = map(int, input().split())
answer = 0
arr = []
save = [20000 for _ in range(m+1)]
for a in range(n):
    arr.append(int(input()))
save[0] = 0
for i in range(n):
    for j in range(arr[i],m+1):
        if (save[j - arr[i]]) != 20000:
            save[j] = min(save[j] , save[j-arr[i]] + 1 )

if save[m] == 20000:
    answer = -1
else:
    answer = save[m]
print(answer)