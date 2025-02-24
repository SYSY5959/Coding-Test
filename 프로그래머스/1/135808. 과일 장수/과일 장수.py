def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    
    box = [score[i*m : (i+1)*m] for i in range((len(score)+m-1) // m )]
    for fruit in box:
        if len(fruit) == m:
            answer += min(fruit)*m
            
    return answer