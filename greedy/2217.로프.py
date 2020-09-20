import sys
n = int(sys.stdin.readline())
rope = [ int(sys.stdin.readline()) for _ in range(n) ]

rope.sort(reverse=True)
res = 0

for a in range(n):
    if rope[a] * (a+1) > res:
        res = rope[a]*(a+1)

print(res)
        
