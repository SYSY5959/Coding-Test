def solution(s):
    answer = ''
    word = s.split(" ")
    for i in range(len(word)):
        for j in range(len(word[i])):
            if j%2 == 0:
                answer += word[i][j].upper()
            else:
                answer += word[i][j].lower()
        answer += " "
    answer = answer[:-1]
    return answer