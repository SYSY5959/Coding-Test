## 이 문제는 DP 
## 가장 오른쪽 끝 가로 2개 or 세로 1개 고정!! -> 피보나치!!!
## d[i] = d[i-1] + d[i-2]

def solution(n):
    # dp 테이블 초기화 (n+1 크기)
    dp = [0] * (n + 1)
    
    if n == 1:
        return 1
    if n == 2:
        return 2
        
    # 초기값 설정
    dp[1] = 1
    dp[2] = 2
    
    # 3부터 n까지 반복문으로 점화식 계산
    for i in range(3, n + 1):
        # 덧셈을 할 때마다 나머지 연산을 적용 !!!!
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
        
    return dp[n]

## 시간 초과로 실패,,,ㅠㅠㅠ
# from itertools import combinations
# def combi(n,r):
#     return len(list(combinations(range(n), r)))

# def solution(n):
#     answer = 0
#     if n % 2 == 0:
#         for i in range((n//2) +1):
#             answer += combi(i+n-i*2, i)
#     if n % 2 != 0:
#         for i in range((n//2) +1):
#             answer += combi(1+i+n-i*2, i)
#     return answer%(1000000007)