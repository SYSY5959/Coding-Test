from collections import deque
    
def solution(board):
    answer = 0
    arr = []
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i,j)
            if board[i][j] == "G":
                end = (i,j)
    def bfs(si,sj,ei,ej):
        nonlocal answer
        v = [[0]*m for _ in range(n)]
        v[si][sj] = 1
        q = deque()
        q.append((si,sj,0)) # 시작열, 시작행, 횟수
        
        while q:
            ci,cj,cnt = q.popleft()
            if (ci,cj) == (ei,ej):
                return cnt
            for di,dj in ((0,-1),(1,0),(0,1),(-1,0)):
                ni,nj = ci,cj   # 여기서 그냥 현재 좌표 찍기
                
                # 벽이나 장애물을 만날 때까지 미끄러지기!! 
                # 위치가 범위를 벗어나거나, 장애물이면 멈춤
                while 0<=ni+di<n and 0<=nj+dj<m and board[ni+di][nj+dj] != "D":
                    ni,nj = ni+di,nj+dj
                
                # 미끄러져 멈춘 위치가 아직 방문하지 않은 곳이라면...
                if v[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni,nj,cnt+1))
                    
        return -1
    
    answer = bfs(start[0],start[1], end[0],end[1])
    
    return answer