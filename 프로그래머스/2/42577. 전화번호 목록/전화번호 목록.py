## 접두어
# 짧은 번호 A / 긴 번호 B
# A의 전체가 B의 시작 부분과 완전히 일치해야 함!!!

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        current = phone_book[i]
        nextlong = phone_book[i+1]
        if nextlong[:len(current)] == current:
            answer = False

    return answer



# def solution(phone_book):
#     answer = True
#     dic = {}
#     for phone in phone_book:
#         ph = phone[0:2] # 접두사
#         ## 접두사 같은 게 있으면 key 값 + 1
#         dic[ph] = dic.get(ph, 0) + 1
#     answer = not (any(v>=2 for v in dic.values()))
#     return answer