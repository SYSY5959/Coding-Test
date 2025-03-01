from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        # ceil: 올림해서 정수 반환
        queue.append(math.ceil((100 - progresses[i])/speeds[i]))
    
    # 여기서부터는 혼자 못 품 ㅠㅠ
    index = 0
    for i in range(len(queue)): 
        if queue[i] > queue[index]:
            answer.append(i - index)
            index = i
    
    # 마지막 리스트 요소 추가
    answer.append(len(queue)-index)
            
    
    return answer