def dfs(c):
    ans_dfs.append(c) # 방문노드 추가
    v[c] = 1 # 방문 표시
    
    for n in adj[c]:
        if not v[n]: # if v[n] == 0 -> 방문하지 않은 노드인 경우 
            dfs(n) # 방문
            
def bfs(s):
    q = [] # 필요한 q, v[], 변수 생성
    
    q.append(s) # q에 초기데이터 삽입
    ans_bfs.append(s)
    v[s] = 1
    
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]: # 방문하지 않은 노드 -> 큐에 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1


n,m,V = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향
    
for i in range(1, n+1):
    adj[i].sort() # 각 노드를 오름차순 정렬

## 메인 블럭 다 만들어 놓고
## 함수는 제일 마지막에 호출!!

v = [0]*(n+1)
ans_dfs = []
dfs(V)

v = [0]*(n+1)
ans_bfs = []
bfs(V)

print(*ans_dfs) # 리스트 안의 요소 출력 (,없이)
print(*ans_bfs)

