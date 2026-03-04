def solution(s):
    answer = True
    s = s.upper()
    p = s.count('P')
    y = s.count('Y')
    if p!=y:
        answer = False
    return answer