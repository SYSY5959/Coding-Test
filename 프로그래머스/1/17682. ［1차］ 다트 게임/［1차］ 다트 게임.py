def solution(dartResult):
    scoresum = []
    num = ''
    for val in dartResult:           
        if val == "S":
            scoresum.append(int(num)**1)
            num = ""
        elif val == "D":
            scoresum.append(int(num)**2)
            num = ''
        elif val == "T":
            scoresum.append(int(num)**3)
            num = ''
        elif val == "*":
            if len(scoresum) == 1:
                scoresum[0] *= 2
            else:
                scoresum[-2] *= 2
                scoresum[-1] *= 2
        elif val == "#":
            scoresum[-1] *= (-1)
            
        ## 숫자 일 때!!  is.digit()으로 확인하면 10을 1,0으로 나눠서 함.
        ## 그래서 문자가 아닐 때, 문자열에 더해주고, SDT에서 int(num)으로. 그리고 다시 num 초기화
        else: 
            num += val
            
    return sum(scoresum)