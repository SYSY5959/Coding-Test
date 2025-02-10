def solution(k, score):
    answer = []
    rank = []
    n = len(score)
    for i in range(n):
        if i < k:
            rank.append(score[i])
            rank.sort(reverse=True)
            answer.append(rank[-1])
        
        mini = rank[-1] # min(score[:i+1])
        
        if i >= k:
            if score[i] > mini:
                rank.pop()
                rank.append(score[i])
                rank.sort(reverse=True)
                answer.append(rank[-1])
            else:
                answer.append(rank[-1])
                
    return answer