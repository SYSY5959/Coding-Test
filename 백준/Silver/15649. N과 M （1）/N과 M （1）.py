n,m = map(int, input().split())

s = []

## DFS - 백트랙킹 -> 아직 더 공부 필요함!!!
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()
 
#### 런타임 에러
#for i in range(1,n):
#    for j in range(1,m):
#        if i != j:
#            print(f"{i} {j}")