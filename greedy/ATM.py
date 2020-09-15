n = int(input())
p = list(map(int,input().split()))

res = 0
p.sort()
for a in range(len(p)):
    res += p[a]*(n-a)
print(res)

