def solution(numbers, target):
    answer = 0
    
    def dfs(index, total):
        nonlocal answer
        if index == len(numbers): # 모든 숫자를 사용했을 때만 체크
            if total == target:
                answer += 1
            return

        dfs(index+1, total+numbers[index])
        dfs(index+1, total-numbers[index])
    
    dfs(0, 0)
    return answer

