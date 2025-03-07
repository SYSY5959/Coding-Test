def dfs(n):
	global ans
	if n == N: # N행까지 진행한 경우의 수 가능: 성공
		ans +=1
		return
	for j in range(N):
		if v1[j] == v2[n+j] == v3[n-j] == 0: # 열/대각선에 방문 가능한지 확인
			v1[j] = v2[n+j] = v3[n-j] = 1 # 방문 표시
			dfs(n+1)
			v1[j] = v2[n+j] = v3[n-j] = 0 # 방문 해제



N = int(input())
v1 = [0]*N # 열 확인 / 행은 확인할 필요 X 현재 행에 대한 함수니까.
v2 = [0]*2*N # 오른쪽 위 대각선 확인
v3 = [0]*2*N # 오른쪽 아래 대각선 확인
ans = 0

dfs(0)
print(ans)