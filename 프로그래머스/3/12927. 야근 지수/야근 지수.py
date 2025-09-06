## 효율적인 코드 : Heap -> 최소 힙 지원. 
## 여기서는 리스트 안의 최댓값을 계속 찾아야하니까 값에 -1 곱해서 최대 힙처럼 사용
import heapq

def solution(n, works):
    # 1. 모든 작업이 n보다 작으면, 최종 결과는 0
    if sum(works) <= n :
        return 0
    
    # 2. works를 최대 힙으로 변환
    # heapq는 리스트 자체를 힙으로 변경 -> 새로운 리스트를 만들어 사용
    max_heap = [-w for w in works]
    heapq.heapify(max_heap)
    
    # 3. n번 만큼 루프 돌며, 가장 큰 값을 1씩 줄이기
    for _ in range(n):
        # 가장 큰 작업량(음수니까 가장 작은 값)을 꺼냄
        largest = heapq.heappop(max_heap)
        
        # 작업량이 남아있으면, 1 더해서 (원래 값에선 1 빼서) 다시 힙에 추가
        if largest < 0:
            heapq.heappush(max_heap, largest+1)

    # 4. 힙에 남은 값들 제곱합 계산
    
    return sum([w**2 for w in max_heap])


## 시간 초과한 알고리즘
# import numpy as np

# def solution(n, works):
#     answer = 0
#     for i in range(n):
#         works[works.index(max(works))] = max(works)-1
#     if min(works) < 0 :
#         answer = 0
#     else:
#         # answer = sum(x**2 for x in works) -> 시간 초과
#         arr = np.array(works)
#         answer = int(np.sum(arr**2))
#     return answer