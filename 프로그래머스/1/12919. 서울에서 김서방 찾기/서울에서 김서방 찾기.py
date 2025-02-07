### 내 풀이
def solution(seoul):
    n = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            n = i
    answer = "김서방은 " + str(n) +"에 있다"
    return answer


### 더 간단한 풀이
def solution(seoul):
    
    answer = ''
    answer = "김서방은 {}에 있다".format(seoul.index('Kim'))
    ## "~~~ {} ~~".format(a) : 문자열 안에 {}에 a 들어감
    
    return answer
