def bfs(s,e):
    q = []
    
    q.append(s)
    v[s] = 1
    
    while q:
        c = q.pop(0)
        # 마지막 노드 도달하면 끝냄!!!1
        if c == e:
            return v[e]-1 # 나와 한칸 떨어져 있으면 촌수:1이니까 자기 자신 제외.
        
        # c와 연결된 번호인 경우 미방문이면 방문!!
        for n in arr[c]:
            if v[n] == 0:
                q.append(n)
                v[n] += v[c]+1
    # 이곳의 코드를 실행했다면.. 연결고리 찾지 못함. 연결고리 없음
    return -1
        

n = int(input()) # 사람 수
S,E = map(int,input().split()) # 촌수 구하고 싶은 두 사람
m = int(input()) # 연결 개수
arr = [[] for _ in range(n+1)]
for _ in range(m):
    p,c = map(int, input().split()) # 연결된 노드
    arr[p].append(c)
    arr[c].append(p)

v = [0]*(n+1)
ans = bfs(S,E)
print(ans)
