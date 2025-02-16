def solution(n):
    answer = n
    
    c = bin(n)[2:].count("1") # 1 개수
    
    while True:
        answer+=1
        if bin(answer).count("1") == c:
            return answer
