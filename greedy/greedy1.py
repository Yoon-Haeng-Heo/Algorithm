def solution():
    n,m,k = map(int,input().split())
    summ = 0
    cnt= 0
    arr = list(map(int,input().split()))
    arr.sort()
    a = arr[n-1]
    b = arr[n-2]

    #cnt는 큰 수가 더해지는 횟수 
    cnt = int(m/(k+1)) * k + (m % (k+1))
    summ = cnt * a + (m-cnt) * b

    return summ
print(solution())