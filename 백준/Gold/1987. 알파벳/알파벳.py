## DFS로 풀면 시간 초과 나옴!
## BFS로!! 특정 좌표에서의 "시퀀스"
from collections import deque

def bfs():
    # q 등 필요 데이터 생성
    q = deque()
    # i,j번째 좌표 도착까지의 시퀀스. 방문했으면 시퀀스 표시
    # v = [[[] for _ in range(C)] for _ in range(R)] 
    # # 시간 초과 : 리스트는 O(N)
    # set으로 하기 : O(1)
    v = [[set() for _ in range(C)] for _ in range(R)]
    ans = 1

    # q에 초기 데이터 삽입
    q.append((0,0,arr[0][0]))
    v[0][0].add(arr[0][0])


    while q:
        ci,cj,cv = q.popleft()
        ans = max(ans,len(cv))
        # 4방향
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            # 범위내, 중복 문자 아닌 경우
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in cv:
                # 중복 시퀀스도 아닌 경우
                if cv+arr[ni][nj] not in v[ni][nj]:
                    q.append((ni,nj,cv+arr[ni][nj]))
                    v[ni][nj].add((cv+arr[ni][nj]))
    return ans


R,C = map(int, input().split())
arr = list(input() for _ in range(R))
ans = bfs()
print(ans)