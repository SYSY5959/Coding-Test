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

## 다른 풀이 : BFS로
def solution(numbers, target):
  leaves = [0]          # 모든 계산 결과를 리스트로 다 담기      
  count = 0 

  for num in numbers : 
    temp = []
	
    # 자손 노드 
    for leaf in leaves : # 앞 단계에서 계산한 리스트에 새로운 숫자 더하고 빼는 경우 다시 담기
      temp.append(leaf + num)    # 더하는 경우 
      temp.append(leaf - num)    # 빼는 경우 

    leaves = temp 

  # 모든 경우의 수 계산 후 target과 같은지 확인 
  for leaf in leaves : 
    if leaf == target : 
      count += 1

  return count
