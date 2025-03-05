## bfs : (x-1, x+1, 2*x) 순회
from collections import deque
def bfs(s,e):
    q = deque()
    q.append(s)
    v[s] = 1
    
    while q:
        c = q.popleft()
        if c == e:
            return v[e]-1
        for n in (c-1, c+1, 2*c):
            if 0<=n<=200000 and v[n]==0:
                q.append(n)
                v[n] = v[c]+1
    return -1


N,K = map(int, input().split())
v = [0]*200001
ans = bfs(N,K)
print(ans)