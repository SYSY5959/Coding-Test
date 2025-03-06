def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n): # i=0,1,2,3,4
        for j in range(i+1,n): # i = 1 -> j = 2,3,4
            if i < j:
                answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()       
    return answer