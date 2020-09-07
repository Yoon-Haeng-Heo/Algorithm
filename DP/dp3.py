n = int(input())

save = [0 for _ in range(n+1)]

save[1] = 1
save[2] = 3
for a in range(3,n+1):
    save[a] = (save[a-1] + 2*save[a-2])

print(save[n] % 796796)