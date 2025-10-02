def solution(keymap, targets):
    answer = []
    dic = {}
    for key in keymap:
        for idx,letter in enumerate(key):
            press = idx + 1
            # 사전에 없는 알파벳이거나 더 작은 인덱스 가진 알파벳 나오면 업데이트
            if letter not in dic or dic[letter] > press:
                dic[letter] = press
    
    for target in targets:
        cnt = 0
        for t in target:
            if t not in dic :
                answer.append(-1)
                break
            else:
                cnt += dic[t]
        
        # 안쪽 for문이 break 없이 정상 실행되었을 때만 실행!!!!
        else:
            answer.append(cnt)
            
    return answer