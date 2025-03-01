from collections import deque

def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)]
    # [(0,2), (1,1), (2,3), (3,2)]
    
    while True:
        cur = queue.pop(0) # queue = [(1,1), (2,3), (3,2)]
        # cur = (0,2)
        if any(cur[1] < q[1] for q in queue): # 우선순위 낮은 애들 빼서 뒤로 넣기
            queue.append(cur) # queue = [(1,1), (2,3), (3,2), (0,2)]
        else: # 더이상 순서 바꿀 필요 없을 때
            answer+=1
            if cur[0] == location:
                return answer