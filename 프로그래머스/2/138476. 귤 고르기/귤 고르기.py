from collections import Counter
# 리스트 요소 별 개수를 딕셔너리로 만들어주는 라이브러리

def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    count = list(Counter(tangerine).values()) ## 딕셔너리 값들만 리스트로 가져오기
    count.sort(reverse = True)
    total, i = 0, 0
    while total < k:
        total+= count[i]
        answer += 1
        i += 1
    
    return answer