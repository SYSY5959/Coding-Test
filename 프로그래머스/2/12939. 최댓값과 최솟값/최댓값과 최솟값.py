def solution(s):
    s = s.split(" ")    
    s = list(map(int, s))
    answer = str(min(s)) + " " + str(max(s))
    
    return answer