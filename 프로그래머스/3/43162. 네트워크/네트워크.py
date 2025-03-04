## dfs : 방문처리 -> for -> if 
def solution(n, computers):
    answer = 0
    arr = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                arr[i+1].append(j+1)
    print(arr)
    
    def dfs(c):
        # dfs : c 입력 받아서 방문
        nonlocal answer
        v[c] = 1 # 방문 처리
        
        for n in arr[c]: # 이웃한 노드
            if v[n] == 0: # 그 노드를 아직 방문하지 않았다면
                dfs(n) # 방문 시작 ~
        
        return
    
    v = [0]*(n+1)
    for i in range(1,n+1): # 모든 노드에 대해 
        if v[i] == 0: # 아직 그 노드를 방문하지 않았다면
            dfs(i) # dfs 출발 (덩어리 찾기)
            answer += 1 # dfs 끝나면 개수 하나 추가 
    return answer