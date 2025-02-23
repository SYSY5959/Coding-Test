def solution(a, b, n):
    answer = 0
    while n >= a:
        count = (n//a) * b # 받은 콜라 개수
        left = n%a # 추가 콜라를 받지 못한 콜라 개수 (나머지)
        answer += count
        n = count + left # 합친 걸로 또 콜라 받기
    return answer
