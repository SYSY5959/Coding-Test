## 혼자 못 품 ㅠㅠ
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


## 다른 풀이

## priorities : 실행대기 큐 , loaction : 추적해야되는 프로세스 인덱스 번호
# 1. 큐에서 왼쪽 요소를 뽑는다
# 2. 뽑은 요소와 왼쪽에 남아있는 큐들과 우선순위를 비교한다
    # 2-1 우선순위가 더 높은게 있다면 뽑은 요소를 오른쪽에 넣는다.
        # 2-1-1 loaction을 변경해서 프로세스 인덱스 번호를 추적한다.        
    # 2-2 우선순위가더 높은게 없다면 loaction을 출력한다.

from collections import deque
    
def solution(priorities, location):
    answer = 0
    deq_list = deque(priorities)

    while True:
        pop=deq_list.popleft()

        # 마지막 요소일때 - 추가된 예외처리
        if len(deq_list)==0:
            return answer+1
    
        # 2번에 해당
        if pop<max(deq_list):
            deq_list.append(pop)
        else:
            answer+=1
            if location==0:
                return answer

        # 위치 추적
        if location==0:
            location=len(deq_list)-1
        else:
            location-=1
