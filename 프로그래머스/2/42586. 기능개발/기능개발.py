from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        # ceil: 올림해서 정수 반환
        queue.append(math.ceil((100 - progresses[i])/speeds[i]))

    # 작업완료까지 걸리는 작업일을 먼저 전부 계산해서 리스트에 담아둔다. 이렇게 한번에 쓰는 방법도 있음!!
    # days = [math.ceil((100-p) / s) for p, s in zip(progresses, speeds)]
    
    
    
    # 여기서부터는 혼자 못 품 ㅠㅠ 
    # 리스트에서 더 큰 값을 가지고 있는 인덱스 업데이트 하고, 그 전까지 개수 구하기
    index = 0
    for i in range(len(queue)): 
        if queue[i] > queue[index]:
            answer.append(i - index)
            index = i
    
    # 마지막 리스트 요소 추가
    answer.append(len(queue)-index)
            
    
    return answer

# 다른 풀이
def solution(progresses, speeds):
    answer = []
    day = 0         # 작업 일수 (배포 날짜)
    count = 0       # 배포된 작업 개수

  # 100 % 인지 확인하는 식 : progresses(현재 작업진도) + day(걸린 일수) * speeds(작업 속도)
    while len(progresses) > 0 :
        if ( progresses[0] + day * speeds[0] ) >= 100 :     # 작업진도가 100% 이상이면
            progresses.pop(0)                               # 작업진도 리스트와
            speeds.pop(0)                                   # 작업속도 리스트에서 삭제한 후
            count += 1                                      # 배포 개수 1 증가

        else :
            if count > 0 :                                  # 현재는 작업진도가 100% 이상이 아닌데, 앞에서 배포할 작업이 있었다면
                answer.append(count)                        # 배포개수를 answer 리스트에 담아준 후
                count = 0                                   # 초기화
            day += 1                                        # 다음 날짜 작업을 확인하기 위해 작업 일수에 하루를 더해줌

    answer.append(count)                                    # 마지막 배포된 작업들에 대해서 append 를 실행하지 않고 while문을 빠져나왔기 때문에 처리해줘야함

    return answer

