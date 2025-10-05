import heapq

# 우선순위 큐(힙) 쓰는 문제!! -> 처음 배움...
N = int(input())
M = int(input())

# 그래프 정보 저장
graph = [[] for _ in range(N+1)]
# 방문 리스트
v = [0]*(N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((c,b)) # (비용, 연결된 노드)
    graph[b].append((c,a)) # 양방향이니까 

total = 0

## 우선순휘 큐(힙) 초기화 & 시작 노드 설정 (1번 컴퓨터로)
# 힙에는 (비용, 노드) 튜플로 저장
pq = [(0,1)]

while pq:
    # 비용이 가장 작은 간선을 힙에서 꺼냄
    cost, cn = heapq.heappop(pq)

    # 이미 방문한 노드면 무시 (사이클 방지)
    if v[cn] == 1:
        continue

    ## 현재 노드 방문 처리, 비용 추가
    v[cn] = 1
    total += cost

    for ncost, nn in graph[cn]:
        if v[nn] == 0:
            heapq.heappush(pq, (ncost,nn))

print(total)