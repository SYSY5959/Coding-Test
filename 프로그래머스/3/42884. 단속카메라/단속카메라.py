
def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    
    cctv = -30001
    for i,j in routes:
        if i > cctv:
            cctv = j
            answer += 1

    return answer