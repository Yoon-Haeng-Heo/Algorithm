n,k = map(int,input().split())
coin = []

for _ in range(n):
    coin.append(int(input()))

coin = sorted(coin,reverse=True)
cnt = 0
for a in coin:
    if k // a > 0:
        if k % a == 0:
            cnt += k // a
            break
        else:
            cnt += k // a
            k = k % a

print(cnt)
