## 이중 for문으로 하면 시간 초과 -> 스택 이용!!
def solution(numbers):
    answer = [-1]*len(numbers)
    stack = [] # 인덱스 넣기
    for i in range(len(numbers)):
        # 현재 숫자가 스택 맨 뒤 인덱스가 가리키는 숫자보다 크면
        # 현재 숫자보다 뒤의 숫자가 더 작은 상황
        while stack and numbers[stack[-1]] < numbers[i]:
            # 스택에서 해상 인덱스 꺼내고, 현재 숫자 저장 
            j = stack.pop()
            answer[j] = numbers[i]
            
        stack.append(i)
    return answer