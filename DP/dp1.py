# bottom-up 방식으로 진행 
# arr라는 배열에서 
#
#
#
def solution(num):
    arr = [0 for _ in range(num+1)]
    
    for a in range(2,len(arr)):
        arr[a] = arr[a-1] + 1   # 어차피 최소 값을 정해주기 때문에 -1을 먼저 해줌(나누기 부터 했을 때 오류 )
        if a % 5 == 0:
            arr[a] = min(arr[a],arr[a//5] + 1)
        if a%3 == 0:
            arr[a] = min(arr[a],arr[a//3] + 1)
        if a%2 == 0:
            arr[a] = min(arr[a],arr[a//2] + 1)
    return arr[num]

print(solution(4))
