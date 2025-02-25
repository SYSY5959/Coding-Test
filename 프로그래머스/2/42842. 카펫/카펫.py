def solution(brown, yellow):
    answer = []
    divisor = []
    n = brown + yellow
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisor.append([i,n//i])
    for mul in divisor:
        if (mul[0]-2)*(mul[1]-2) == yellow:
            answer = mul
    if answer[0] < answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
    return answer