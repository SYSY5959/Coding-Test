def solution(n):
    answer = 0
    num = []
    for i in str(n):
        num.append(i)
    
    num.sort(reverse = True)
    answer = "".join(num)
    return int(answer)