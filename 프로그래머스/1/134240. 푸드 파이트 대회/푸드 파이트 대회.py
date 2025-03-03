import math
def solution(food):
    answer = '0'
    for i in range(len(food)-1,0,-1):
        n = math.floor(food[i]/2)
        answer = str(i)*n + answer + str(i)*n
        print(answer)
    return answer