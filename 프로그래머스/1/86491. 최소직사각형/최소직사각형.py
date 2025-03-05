def solution(sizes):
    answer = 0
    for name in sizes: # 리스트 안에 [작은 수, 큰 수]
        if name[0] > name[1]:
            name[0],name[1] = name[1],name[0]
    wmax = 0
    hmax = 0
    for w in sizes:
        if w[0] > wmax:
            wmax = w[0]
    for h in sizes:
        if h[1] > hmax:
            hmax = h[1]
    answer = hmax*wmax
        
    return answer