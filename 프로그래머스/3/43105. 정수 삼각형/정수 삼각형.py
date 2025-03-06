## 최댓값 : 이전 단계에서 a[2][1] <- max(a[1][0], a[1][1])

def solution(triangle):
    n = len(triangle)
    dp = [row[:] for row in triangle]  # 깊은 복사
    
    # triangle index: i = 0~n-1까지 -> j = 0~i까지 
    # 모든 층 순회 위에서부터 1,2,,,n-1층 (0층은 계산할 필요 X)
    # DP 문제에서 0을 계산할 필요 없음. 미리 지정해두기 때문!!
    for i in range(1,n): 
        for j in range(i+1): # j: 현재 층에서의 인덱스
            if j == 0: 
                left = 0
            else:
                left = dp[i-1][j-1]
            if j == i: ## 오른쪽 끝이니까, i=j일 때
                right = 0
            else:
                right = dp[i-1][j]
            dp[i][j] = dp[i][j] + max(left, right)
    
    return max(dp[n-1])