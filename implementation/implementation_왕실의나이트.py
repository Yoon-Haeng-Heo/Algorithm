def solution():
    data = input()
    row = int(data[1])
    col = int(ord(data[0])) - int(ord('a'))+1   # 알파벳으로 위치 알 수 있게

    direct = [(-2,-1),(2,-1),(-2,1),(2,1),(1,2),(1,-2),(-1,-2),(-1,2)] # 갈 수 있는 방향

    cnt = 0 

    for a in direct:
        nx = row + a[0]
        ny = col + a[1]

        if nx>=1 and nx <= 8 and ny >=1 and ny <=8:
            cnt += 1
    return cnt
print(solution())