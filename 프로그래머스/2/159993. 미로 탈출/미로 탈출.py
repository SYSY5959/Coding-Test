## 시작 -> 레버 -> 도착 : BFS 두번하고 두개 cnt 더해주기
## 미로찾기 문제는 BFS로 !!! 
from collections import deque

def solution(maps):
    answer = 0
    n = len(maps) # 행
    m = len(maps[0]) # 열
    
    def bfs(si,sj,ei,ej):
        q = deque()
        v = [[0]*m for _ in range(n)]

        q.append((si,sj,0)) # (시작 행, 시작 열, 거리)
        v[si][sj] = 1

        while q:
            ci,cj,dist = q.popleft()
            # 종료 조건
            if (ci,cj) == (ei,ej):
                return dist
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<n and 0<=nj<m and v[ni][nj] == 0 and maps[ni][nj] != "X":
                        v[ni][nj] = 1
                        q.append((ni,nj,dist+1))
        
        # 큐가 비어있는데 목표에 도달 X
        return -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i,j)
            if maps[i][j] == "L":
                lever = (i,j)
            if maps[i][j] == "E":
                end = (i,j)
                
    tolever = bfs(start[0],start[1], lever[0],lever[1])
    toend = bfs(lever[0],lever[1], end[0],end[1])
    
    if tolever==-1 or toend==-1:
        answer = -1
    else:
        answer = tolever+toend
    
    return answer