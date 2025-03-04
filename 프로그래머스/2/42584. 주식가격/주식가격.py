from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        a = queue.popleft() # 3 : 현재 주식 가격
        s = 0
        for q in queue: #[2,3] : 이후 주식 가격
            s +=1
            if q < a: # 현재 가격보다 주식 가격이 떨어질 때
                break
        answer.append(s)          
        
    return answer