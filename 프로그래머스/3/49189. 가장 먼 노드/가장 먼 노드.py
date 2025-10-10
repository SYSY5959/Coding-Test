## 1에서 최단거리가 가장 먼 노드 구하기 
# -> '최단거리'니까 BFS. DFS는 최단경로 보장을 못함
from collections import deque

def solution(n, edge):
    answer = 0
    g = [[] for _ in range(n+1)]
    v = [-1]*(n+1) # 거리 배열 : -1 초기화
    for i,j in edge:
        g[i].append(j)
        g[j].append(i)
    
    ## BFS 시작
    v[1] = 0
    q = deque()
    q.append(1)

    while q:
        c = q.popleft()
        for n in g[c]:
            if v[n] == -1: # 미방문
                v[n] = v[c] + 1
                q.append(n)
    
    ## 가장 먼 노드 찾기. 거리에서 최댓값 찾기
    answer = v.count(max(v))

    return answer