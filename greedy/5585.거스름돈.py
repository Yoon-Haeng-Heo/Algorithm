coin = [500,100,50,10,5,1]

money = 1000 - int(input())

cnt = 0
for a in coin:
    if money >= a:
        cnt += (money // a)
        money %= a

print(cnt)


