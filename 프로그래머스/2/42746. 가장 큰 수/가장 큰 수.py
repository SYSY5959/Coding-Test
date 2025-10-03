def solution(numbers):
    answer = ''
    
    # 숫자 문자열을 정렬하면 사전식으로 정렬됨 
    # ['9', '5', '34', '30', '3'] 근데 여기서 30과 3의 자리를 바꾸고 싶으면
    # sorted함수에서 key로 커스텀. "3030303030.." vs "3333333.." 비교하게 됨

    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    #answer = "".join(numbers) -> 이렇게 하면 [0,0] 일때 '00'이 나옴!!!
    answer = str(int("".join(numbers)))

    return answer
