def solution(k, d):
    answer = 0
    n = d//k
    for i in range(n+1):
        y_max = (d**2 - (k*i)**2)**0.5
        answer += y_max//k + 1 

    return answer