n = int(input())
data = list(map(int,input().split()))
cnt = 0
data.sort()

for a in range(1,n+1):
    if a <= data.count(a):
        cnt += 1

print(cnt)