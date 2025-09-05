from collections import deque
def bfs(s,x,n,v):
    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == x:
            return v[c]-1
        next_lst = [c-n]
        if c % 2 == 0:
            next_lst.append(c//2)
        if c % 3 == 0:
            next_lst.append(c//3)

        for ne in next_lst:
            if ne>0 and v.get(ne,0)==0:
                v[ne] = v[c]+1
                q.append(ne)
    return -1

def solution(x, y, n):

    v = {}
    answer = bfs(y,x,n,v)
    
    return answer