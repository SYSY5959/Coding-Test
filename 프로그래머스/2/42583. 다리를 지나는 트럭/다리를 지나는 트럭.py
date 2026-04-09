# 다리에는 최대 bridge_length 대
# 다리는 최대 weight까지 버틸 수 있음
# 내려가는 게 먼저임. 내려가고 올라가야함.
# 다리에 길이(= bridge_length) 도 있음.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    arrive = 0 # 몇 대가 도착했는지를 확인할 거임. 그리고 arrive = len(truck_weights) 종료
    bb = deque([0]*bridge_length)
    answer = 0
    total = 0 # 다리 위에 올라가 있는 트럭의 무게의 합
    
    while arrive < len(truck_weights):
        a = bb.popleft() # 앞에 트럭 밀기
        total -= a
        if a != 0:
            arrive += 1
        
        if len(queue) > 0:
            candidate = queue[0] 
        else:
            candidate = 0
            
        if total + candidate <= weight: # 현재 다리 무게 + 들어올 트럭 무게
            if len(queue) > 0:
                current = queue.popleft() # 현재 트럭 무게 
            else:
                current = 0
            bb.append(current) # 다리에 트럭 올리기
            total += current
            
        else:
            bb.append(0)

        answer +=1
    
    return answer