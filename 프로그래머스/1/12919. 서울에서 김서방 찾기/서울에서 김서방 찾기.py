def solution(seoul):
    n = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            n = i
    answer = "김서방은 " + str(n) +"에 있다"
    return answer