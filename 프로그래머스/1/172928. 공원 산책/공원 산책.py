def nextt(ci,cj,park,op,n):
    dic = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    di,dj = dic[op]
    ni,nj = ci,cj

    for _ in range(n):
        ni,nj = ni+di,nj+dj
        
        # 장애물이 있으면,,
        if not(0<=ni<len(park) and 0<=nj<len(park[0]) and park[ni][nj] != "X"):
            return ci,cj
    return ni,nj

def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                ci,cj = i,j
                break
    for route in routes:
        op,n_str = route.split()
        n = int(n_str)
        ci,cj = nextt(ci,cj,park,op,n)
                
    return [ci,cj]