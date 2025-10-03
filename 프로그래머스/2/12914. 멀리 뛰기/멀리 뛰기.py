## DP로 푸는 문제
# 피보나치 수열

def solution(n):
    # n이 1,2일 때 먼저 처리해줘야함!! 순서 중요..
    if n==1 or n==2:
        return n
    
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    
    
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n]

# ## DFS로 풀었는데, 시간 초과 나옴;; -> DP로 푸는 문제
# def solution(n):
#     answer = 0
#     def dfs(n):
#         nonlocal answer
        
#         for d in [-1,-2]:
#             c = n+d
#             if c == 0:
#                 answer += 1
#             if c > 0:
#                 dfs(c)

#     dfs(n)
#     return answer