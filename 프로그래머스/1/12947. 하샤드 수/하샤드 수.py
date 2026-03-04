def solution(x):
    answer = True
    num = sum(int(i) for i in str(x))
    if x % num != 0:
        answer = False
    
    return answer