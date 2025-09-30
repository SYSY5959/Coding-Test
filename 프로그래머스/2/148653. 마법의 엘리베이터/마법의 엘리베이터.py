def solution(storey):
    answer = 0
    while storey > 0:
        last_digit = storey%10
        next_digit = (storey//10)%10 # 마지막 자리수 5 처리할 때 필요
        # 층수 올라가야할 때
        if last_digit > 5:
            storey += (10-last_digit)
            answer += (10-last_digit)
        # 층수 내려가야할 때
        elif last_digit < 5:
            storey -= last_digit
            answer += last_digit
        # 일의자리가 5일 땐, 그 앞자리 수 보고 결정
        else:
            if next_digit >= 5: # 올라가기
                storey += (10-last_digit)
                answer += (10-last_digit)
            else:   # 내려가기
                storey -= last_digit
                answer += last_digit
                
        # 처리된 일의자리 없애기        
        storey //= 10
                 
    return answer