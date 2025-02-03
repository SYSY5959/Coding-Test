def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget = budget - i
        if budget < 0 :
            break
        answer += 1            
    return answer

### 다른 사람 풀이

#def solution(d, budget):
#    d.sort()
#    while budget < sum(d):
#        d.pop()
#    return len(d)