## Sort 
*created at 2020 09 14*

#### 정렬 문제의 유형
+ 정렬 라이브러리로 풀 수 있는 문제 : 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다.
+ 정렬 알고리즘의 원리에 대해서 물어보느 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
+ 더 빠른 정렬이 필요한 문제 : 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 count sort 등의 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.

#### Selection Sort (선택 정렬)

+ 배열 전체를 돌면서 가장 작은 값(정렬하려고 하는 순서에 따라 다름)을 찾아 맨 앞 요소와 swap하는 형식

```python
    def selection_sort(arr):
        for i in range(len(arr)):
            min_index = i # 가장 작은 원소의 인덱스를 저장
            for j in range(i+1,(len(arr))):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]  # Swap
        return arr
```

+ selection sort의 시간 복잡도는 O(n^2)이다.

#### Insertion Sort (삽입 정렬)

+ 데이터를 확인하면서 각 데이터를 적절한 위치에 삽입하는 형식

```python
    def insertion_sort(arr):
        for i in range(1,len(arr)):
            for j in range(i,0,-1):
                if arr[j] < arr[j-1] :
                    arr[j],arr[j-1] = arr[j-1],arr[j]
                else:
                    break
        return arr
```
+ insertion sort의 시간 복잡도는 O(N^2)이지만 최선의 경우는 O(N)을 가진다. 
+ 그 최선의 경우는 배열이 거의 정렬이 되어 있는 상태

#### Quick sort (퀵 정렬)

+ pivot을 기준으로 나눠서 진행하는 형식
```python
    def quick_sort(arr,start,end):
        if start >= end:
            return
        pivot = start
        left = start + 1
        right = end
        while left <= right:
        # pivot 보다 큰 데이터를 찾을 때 까지 반복
            while left <= end and arr[left] <= arr[pivot]:
                left += 1
        # pivot 보다 작은 데이터를 찾을 때 까지 반복
            while right > start and arr[right] >= arr[pivot]:
                right += 1
            if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
                arr[right],arr[pivot] = arr[pivot],arr[right]
            else:
                arr[left],arr[right] = arr[right],arr[left]
            # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
            quick_sort(arr,start,right-1)
            quick_sort(arr,right+1,end)
        
```

+ 조금 더 python스럽게 코드를 짜본 방법
```python
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        tail = arr[1:] # pivot을 제외한 리스트

        left = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
        right = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

        # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
        return quick_sort(left) + [pivot] +quick_sort(right)
```
+ quick sort의 시간 복잡도는 O(NlogN)이다.

#### Count sort (계수 정렬)

+ count sort는 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.
+ 일반적으로 모든 데이터가 양의 정수이고 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효율적이다.
+ 그 이유는 count sort를 할 때는 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 하기 때문이다.
```python
    def count_sort(arr):
        count = [0] * (max(arr) + 1)
        resarr = []
        for i in range(len(arr)):
            count[arr[i]] += 1      # 각 데이터에 해당하는 인덱스의 값 증가
        for i in range(len(count)):
            for j in range(count[i]):
                resarr.append(i)
        return resarr
```
+ count sort의 시간 복잡도는 데이터의 개수를 N, 최대값의 크기를 K라고 할 때 O(N + K)이다.

#### python의 sort 라이브러리

+ sort()와 sorted() 
+ 정렬 라이브러리는 항상 O(nlogn)의 시간복잡도를 보장한다.
