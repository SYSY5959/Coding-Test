from collections import deque

def solution(n):
    answer = 0
    queue = deque()
    
    for i in range(1, n+1):
        queue.append(i) # 1부터 하나씩 추가
        
        # 합 n보다 크면, 젤 앞에 있는 애들 삭제. sum < n 될 때까지
        while sum(queue) > n: 
                queue.popleft()
                
        if sum(queue) == n:
            answer += 1
            
    return answer