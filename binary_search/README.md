## Binary Search (이진 탐색)
*created at 2020 09 15*

#### 일반적인 순차 탐색
- 리스트 안에 있는 특정 데이터를 찾기 위해 앞에서부터 리스트를 순차적으로 탐색하는 방법
- 시간 복잡도는 O(N)을 가진다.
- 파이썬에서는 count() 메소드가 그 역할을 담당한다.

#### 이진 탐색

- 리스트를 미리 정렬을 한 후에 진행
- 찾으려는 데이터가 반을 나눴을 때 중간 지점을 기준으로 어디에 있는지 확인
- 위 과정을 반복하는 것
- 절반씩 줄어들기 때문에 시간 복잡도는 O(nlogn)을 갖는다.

```python
    def binary_search(arr,target,start,end):
        if start > end :
            return None
        mid = (start + end )//2
        if target == mid :
            return mid
        elif arr[mid] > target:
            return binary_search(arr,target,start,mid-1)
        else:
            return binary_search(arr,target,mid+1,end)
```

#### 이진 탐색 트리

```
      30
  17     48
5  23  37  50
```

#### 빠르게 입력받기

```python
import sys
data = sys.stdin.readline().rstrip()
```