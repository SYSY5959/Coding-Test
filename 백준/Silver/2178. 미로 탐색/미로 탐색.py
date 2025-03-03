def bfs(si,sj,ei,ej):
    q = []
    v = [[0]*m for _ in range(n)] # 행 n개, 열 m개
    
    q.append((si,sj))
    v[si][sj] = 1 # 방문 표시
    
    while q:
        ci,cj = q.pop(0)
        if (ci,cj) == (ei,ej):
            return v[ei][ej]
        # 4방향, 범위 내, 조건에 맞으면: arr==1, v==0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni ,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1

n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)] # 문제에서 주어진 배열

ans = bfs(0,0,n-1, m-1) # 시작 좌표, 끝 좌표
print(ans)

### 또 다른 풀이
from collections import deque

# N, M 입력 받기
n, m = map(int, input().split())

# 2차원 리스트로 미로 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽(0)인 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            # 처음 방문하는 길(1)인 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 도착 지점의 최단 거리 반환
    return graph[n-1][m-1]

# BFS 실행 후 최단 거리 출력
print(bfs(0, 0))
