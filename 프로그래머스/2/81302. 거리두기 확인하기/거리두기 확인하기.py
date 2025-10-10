from collections import deque

def bfs(si,sj,room):
    v = [[0]*5 for _ in range(5)]
    v[si][sj] = 1
    q = deque()
    q.append((si,sj,0))

    while q:
        ci,cj,dist = q.popleft()
        # 시작점 제외하고 다른 사람(P)를 만났을 때, 거리가 2 이하면
        if 0<dist<=2 and room[ci][cj] == 'P':
            return False
        if dist>2:
            continue
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5: 
                if room[ni][nj] != 'X' and v[ni][nj]==0:
                    v[ni][nj] = 1
                    q.append((ni,nj,dist+1))
    return True


def solution(places):
    answer = []

    for room in places:
        is_safe = True
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    # bfs 결과가 False이면, 바로 판단 끝
                    if bfs(i,j,room) == False:
                        is_safe = False
                        break
            if is_safe == False:
                break
        if is_safe == True:
            answer.append(1)
        elif is_safe == False:
            answer.append(0)
    
    return answer