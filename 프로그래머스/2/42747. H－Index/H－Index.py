# H-Index : 내림차순 정렬 -> 논문 순위(N) <= 인용 횟수(C) 인 최대 N 찾기
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        
        # 인용 횟수가 순위보다 작아지는 순간
        if citations[i] < i+1:
            return i
        
    # 모든 논문이 조건을 만족할 경우 (ex. [6,5,4] -> h=3)
    return len(citations)
