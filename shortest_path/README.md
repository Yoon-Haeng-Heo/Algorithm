## Shortest Path (최단 경로)

- 보통 사용하는 최단 거리 알고리즘은 다익스트라, 플로이드 워셜, 벨만 포드 알고리즘 3가지
- 보통 다익스트라와 플로이드-워셜이 자주 출제됨

#### Dijkstra Shortest path algorithm(다익스트라 최단 경로 알고리즘)
- 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다.
- edge의 weight가 음수가 아닐 경우에 적용됨.
- 알고리즘의 원리
    <ol>
    1. 출발 노드를 설정한다.<br>
    2. 최단 거리 테이블을 초기화 한다.<br>
    3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.<br>
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.<br>
    5. 위 과정에서 3과 4를 반복한다.<br>
    </ol>
```python
    import heapq
    import sys
    input = sys.stdin.readline
    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

    # 노드의 개수, 간선의 개수를 입력받기
    n, m = map(int, input().split())
    start = int(input())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [ [] for i in range(n+1)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance =[INF] * (n+1)

    # 모든 간선 정보를 입력받기
    for _ in range(m):
        a,b,c = map(int,input().split())
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[a].append((b,c))
        
    def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:   # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
    dijkstra(start)
        
    for i in range(1,n+1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])
```

    - 위 알고리즘의 시간 복잡도는 O(ElogV)이다. V는 노드의 개수이고 E는 간선의 개수를 의미한다.
    - 방문할 노드들을 list로 하나하나 보는 방법보다 훨씬 효율적인 방법이다. ( O(V^2) 보다 훨씬 빠름)

#### Floyd-Warshall Algorithm (플로이드 워셜 알고리즘) 
- 2차원 리스트에 '최단 거리' 정보를 저장한다는 특징이 다익스트라와 차이점이다.
- N번에 단계에서 O(n^2)의 시간이 소요되므로 총 시간복잡도는 O(N^3)이다.
- 다익스트라 알고리즘은 그리디 알고리즘, 플로이드 워셜 알고리즘은 다이나믹 프로그래밍.
```python
    INF = int(1e9) 

    n = int(input())
    m = int(input())

    # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
    graph= [[INF] * (n+1) for _ in range(n+1)]
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a==b:
                graph[a][b] = 0
    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for _ in range(m):
        # A에서 B로 가는 비용은 C라고 설정
        a,b,c= map(int,input().split())
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
    # 결과 출력
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][b] == INF:
                print("INFINITY",end = ' ')
            else:
                print(graph[a][b],end=' ')
        print()
```