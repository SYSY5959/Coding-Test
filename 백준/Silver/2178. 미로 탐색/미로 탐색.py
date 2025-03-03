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