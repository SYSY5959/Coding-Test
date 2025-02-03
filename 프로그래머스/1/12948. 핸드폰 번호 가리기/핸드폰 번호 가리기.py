## 더 간단한 풀이
def hide_num(s):
    return "*"*(len(s)-4) + s[-4:]

## 내 풀이
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
