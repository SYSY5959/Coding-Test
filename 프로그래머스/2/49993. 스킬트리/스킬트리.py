from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        queue = deque(skill)
        check = True    # 스킬이 순서대로면 True
        
        for s in tree:  # "BACDE"
            if s not in queue:
                continue
            else:
                if s == queue[0]:   # 무조건 젤 처음 원소부터 시작해야함
                    queue.popleft()
                else:
                    check = False
                    break
        if check :
            answer += 1

    return answer