def solution(s):
    answer = ''

    if len(s) % 2 == 0:
        start = len(s) // 2
        answer = s[start-1] +s[start]
    else:
        start = len(s) // 2
        answer = s[start]
    return answer