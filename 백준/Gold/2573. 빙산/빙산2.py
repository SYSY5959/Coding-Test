### 시간 초과 코드

from collections import deque

## 1년 뒤의 빙산 -> 여기서는 주변 바다 개수만 계산하기
def melt(ci,cj):
    cnt = 0
    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
        ni,nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
            cnt +=1
    # arr[ci][cj] = max(arr[ci][cj] - cnt,0)
    return cnt

def bfs(si,sj,v):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] != 0:
                q.append((ni,nj))
                v[ni][nj] = 1

## 빙산 개수 세기
def check(arr):
    # 메번 visited 배열 초기화 해야함!!
    v = [[0]*M for _ in range(N)]
    num = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and v[i][j] == 0:
                bfs(i,j,v)
                num +=1
    return num


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

year = 0
while True:
    
    cnt = check(arr) # 빙산의 개수

    if cnt >= 2:
        print(year)
        break
    if cnt == 0:
        print(0)
        break

    # 올해 녹을 양을 저장해두기!! (i,j) 모든 행렬에           
    dec = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                dec[i][j] = melt(i,j)
    
    # 라운드 종료 시 일괄 반영
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                arr[i][j] = max(0, arr[i][j] - dec[i][j])

    year += 1
