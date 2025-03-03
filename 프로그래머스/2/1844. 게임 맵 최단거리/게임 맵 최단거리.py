## bfs 문제 : q,v 선언 -> 방문 처리 -> while -> pop -> if -> for -> if

def bfs(si,sj,ei,ej,n,m,maps):
    q = []
    v = [[0]*m for _ in range(n)]

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.pop(0)
        if (ci,cj) == (ei,ej):
            return v[ei][ej]
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci + dx, cj + dy
            if 0<=ni<n and 0<=nj<m and maps[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] +1

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs(0,0,n-1,m-1,n,m,maps)
    return answer if answer is not None else -1