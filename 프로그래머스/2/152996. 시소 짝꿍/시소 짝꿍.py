from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for k,v in counter.items():
        # 무게 같은 애들은 nC2 추가
        if v >= 2:
            answer += (v*(v-1))//2
    
    # 이제 무게 같은 애들 없이 각자 짝꿍 카운트
    unique = list(set(weights))
    
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            w1 = unique[i]
            w2 = unique[j]
            if (w1*2 == w2*3 or w1*2 == w2*4 or w1*3 == w2*4 or
                w1*3 == w2*2 or w1*4 == w2*2 or w1*4 == w2*3):
                answer += counter[w1]*counter[w2]
    
    return answer