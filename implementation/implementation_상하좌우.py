def solution():
    n = int(input())
    move = input().split()

    #시작점
    locx = 1
    locy = 1
    x = 0
    y = 0

    mloc = ['L','R','U','D']    #이동 방향을 나타낼 변수
    
    dx = [0,0,-1,1]
    dy = [-1, 1, 0, 0]
    mdict = {'L':(-1,0),'R':(1,0), 'U':(0,1), 'D':(0,-1)}

    for a in move:
        for b in range(len(mloc)):
            if a == mloc[b]:
                x = locx + dx[b]
                y = locy + dy[b]
        if x > n or x <1 or y <1 or y>n:
            continue
        locx = x
        locy = y
    
    print(locx,locy)
solution()

                
