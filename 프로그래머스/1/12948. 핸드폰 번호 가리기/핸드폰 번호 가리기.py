def solution(phone_number):
    p = list(phone_number)
    answer = []
    n = len(p)
    for i in range(n):
        if i < n-4:
            answer.append("*")
        else:
            answer.append(p[i])
        
    answer = "".join(answer)
        
    return answer