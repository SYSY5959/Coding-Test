def solution(k, dungeons):
    answer = 0
    v = [0]*len(dungeons)
    
    def dfs(left,cnt):
        nonlocal answer
        # 현재까지 탐험 횟수로 answer 업데이트
        answer = max(cnt, answer)
        
        for i in range(len(dungeons)):
            if v[i] == 0 and left >= dungeons[i][0]:
                v[i] = 1 # 방문 표시
                # 다음 탐색으로 넘어감
                dfs(left-dungeons[i][1], cnt+1)
                v[i] = 0  # [중요!] 방문 표시를 다시 해제 (백트래킹)
    dfs(k,0)
    return answer