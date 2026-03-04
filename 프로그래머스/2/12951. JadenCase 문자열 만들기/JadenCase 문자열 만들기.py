def solution(s):
    answer = ''
    word = s.split(" ")
    for w in word:
        answer += w.capitalize()
        answer += ' '
            
    answer = answer[:-1]
    return answer