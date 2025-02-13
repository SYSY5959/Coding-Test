def solution(s):
    answer = []
    for i in range(len(s)):
        if s[:i].find(s[i]) == -1:
            answer.append(-1)
        else :
            idx = i - s[:i].rfind(s[i])
            answer.append(idx)
            
    return answer