def solution(n, words):
    checked = [words[0]] # 이전에 쓴 단어인지 확인용
    
    for i in range(1,len(words)):
        if words[i-1][-1] == words[i][0] and words[i] not in checked:
            checked.append(words[i]) # checked에 있는 단어인지 확인하고 추가
        else:
            return [i%n +1 , i//n +1]
    
    return [0,0]

## 더 간단한 풀이
def solution(n, words):
    
    for i in range(1, len(words)):
        #글자가 맞지 않을 때
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    
    return [0,0]
