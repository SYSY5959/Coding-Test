# 한 뭉텅이 안에 들어있는 아파트 개수 세기 -> BFS
def bfs(si,sj): # 한 뭉텅이 개수 세기
    q = []
    q.append((si,sj))    # 큐에 초기 데이터 삽입
    v[si][sj] = 1 # 방문표시
    cnt = 1        # 정답 관련 작업
    
    while q:
        ci,cj = q.pop(0)
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            # 4방향, 범위 내, 미방문이면 큐 삽입
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)] # 입력받은 아파트 정보: 2차원 리스트(행렬) 형식
v = [[0]*n for _ in range(n)] # 방문: 행렬로 만들어주기
ans = [] # 정답을 리스트로 추출

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == 0: # 방문 가능한 곳 미방문이면 방문!!
            ans.append(bfs(i,j))

ans.sort() # 내림차순 정렬 (작은 개수부터)            
print(len(ans), *ans, sep = "\n")
