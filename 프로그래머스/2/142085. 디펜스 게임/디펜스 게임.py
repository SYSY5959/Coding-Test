## 리스트로 풀면 시간초과 -> heapq로 푸는 문제
import heapq
def solution(n, k, enemy):
    answer = 0
    # 지나온 적 수 저장할 힙 (무적권 쓸 정도는 아닌 적들)
    heap = []
    
    for e in enemy:
        # 현재 라운드 힙에 추가
        heapq.heappush(heap, e)
        
        # 무적권으로 막을 수 없는 적들
        if len(heap) > k:
            # 가장 작은 애 꺼내서 막기 -> heappop은 가장 작은 애 나옴
            min_enemy = heapq.heappop(heap)
            n -= min_enemy
        
        # 병력이 바닥 났으면 종료
        if n < 0:
            return answer
        
        answer +=1
         
    return answer