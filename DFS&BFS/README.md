## DFS/BFS

+ stack 과 queue가 기본이 되는 자료구조

#### Stack

+ 후입선출(Last In First Out)
+ python으로는 list를 통해서 append와 pop을 통해서 구현하도록 한다

#### Queue

+ 선입선출(First In First Out)
+ Python에서는 일반 list를 활용하기 보다는 collections 모듈에서 제공하는 deque를 활용하도록 한다.

#### Deque

+ Queue와 같은 원리지만 데이터를 넣고 빼는 것에 있어서 시간이 빠르고 효율적이다.

|  | 리스트 | deque |
|---|:---:|---:|
| 가장 앞 쪽에 원소 추가 | `O(N)` | `O(1)` |
| 가장 뒤 쪽에 원소 추가 | `O(1)` | `O(1)` |
| 가장 앞 쪽에 있는 원소 제거 | `O(N)` | `O(1)` |
| 가장 뒤 쪽에 있는 원소 제거 | `O(1)` | `O(1)` |


```python
deque.appendleft(data)
deque.popleft()
```


### DFS(깊이 우선 탐색)

+ 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
+ 시작 노드부터 인접 노드 중 가장 숫자가 작은 노드를 방문하고 방문한 노드를 스택에 넣고 스택에 들어있는 노드의 인접 노드가 모두 방문이 되었을 때 스택에서 꺼낸다
```python
    def dfs(graph, v,visited):
        # 현재 노드를 방문 처리
        visited[v] = True
        print(v,end =' ')
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if not visited[i]:
                dfs(graph,i,visited)
```

### BFS(너비 우선 탐색)

+ 그래프에서 가까운 노드부터 탐색하는 알고리즘
+ 동작 방식
    - 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
    - 두 번째 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
    def bfs(graph,start,visited):
        # 큐(Queue) 구현을 위해 deque 라이브러리 사용
        queue = deque([start])
        # 현재 노드를 방문 처리
        visited[start] = True
        # 큐가 빌 때까지 반복
        while queue:
            #큐에서 하나의 원소를 뽑아 출력
            v = queue.popleft()
            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
```
| | DFS | BFS |
|---|:---:|---:|
| 동작 원리 | 스택 | 큐 |
| 구현 방법 | 재귀 함수 이용 | 큐 자료구조 이용 |

