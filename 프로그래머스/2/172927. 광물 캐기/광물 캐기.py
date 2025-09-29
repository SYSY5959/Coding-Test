## 그리디 알고리즘!!! 
# -> 다이아몬드 광물이 젤 많은 순서대로 빨리 캐기

from collections import Counter

def solution(picks, minerals):
    answer = 0
    total = sum(picks)*5
    if total < len(minerals):
        minerals = minerals[:total]
    
    ## 광물을 5개로 끊어서 광물 개수 요약 (#dia , #iron, #stone)
    summary = []
    for i in range(0,len(minerals),5):
        cnt = Counter(minerals[i:i+5])
        summary.append((cnt["diamond"], cnt['iron'], cnt['stone']))
    
    # 다이아 많은 순서대로 정렬
    summary.sort(reverse = True)
    
    for dia,iron,stone in summary:
        if picks[0] > 0 :
            answer += dia*1 + iron*1 + stone*1
            picks[0] -= 1
            
        elif picks[1] > 0 : 
            answer += dia*5 + iron*1 + stone*1
            picks[1] -= 1
            
        elif picks[2] > 0 : 
            answer += dia*25 + iron*5 + stone*1
            picks[2] -= 1
            
    return answer