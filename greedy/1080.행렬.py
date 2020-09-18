n,m = map(int,input().split())
cnt = 0
Adata = []
Bdata = []
for _ in range(n):
    Adata.append(list(map(int,input())))
for _ in range(n):
    Bdata.append(list(map(int,input())))

#print(Adata)
def swap(arr,x,y):
    for a in range(3):
        for b in range(3):
            arr[x+a][y+b] = 1 - arr[x+a][y+b]

for a in range(0,n-2):
    for b in range(0,m-2):
        if Adata[a][b] != Bdata[a][b]:
            swap(Adata,a,b)
            #print(Adata)
            #print(Bdata)
            #print(a,b)
            cnt += 1
        
if Adata != Bdata :
    print(-1)
else:
    print(cnt)