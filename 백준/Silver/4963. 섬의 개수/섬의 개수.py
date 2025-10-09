from collections import deque

def bfs(x, y, visited, graph, w, h):
    # 시작점을 큐에 넣고 방문 처리
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    
    while q:
        cx, cy = q.popleft()

        # 8방향 (행 변화량, 열 변화량) 탐색
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for di, dj in directions:
            nx, ny = cx + di, cy + dj
            
            # 지도 범위를 벗어나지 않는지 확인
            if 0 <= nx < h and 0 <= ny < w:
                # 위치가 섬이고, 아직 방문하지 않은 땅이라면
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1 # 방문 처리
                    q.append((nx, ny))  # 큐에 추가

while True:
    w, h = map(int, input().split())
    
    # 입력의 마지막 줄인 경우 루프 종료
    if w == 0 and h == 0:
        break
    
    # 지도 정보 입력받기
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    # 섬들의 방문 상태가 전체 탐색 과정에서 계속 유지되어야 하니까 bfs 함수 밖에서 정의
    visited = [[0] * w for _ in range(h)]

    island_count = 0
    
    # 지도의 모든 좌표를 확인
    for i in range(h):
        for j in range(w):
            # 아직 방문하지 않은 땅(1)을 발견하면
            if graph[i][j] == 1 and visited[i][j] == 0:
                # 연결된 모든 땅을 탐색하고 방문 처리
                bfs(i, j, visited, graph, w, h) # i,j와 연결된, 딱 하나의 섬(연결된 덩어리)만 완벽하게 탐색하고 종료
                island_count += 1 # 섬의 개수 1 증가
    
    print(island_count)