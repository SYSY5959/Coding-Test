## 정답 코드
def solution(N, stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)

## 내 코드 -> 런타임 에러
def solution(N, stages):
    answer = []
    rate = []
    for i in range(1,N+1):
        #fil = list(filter(lambda x: x>=i, stages))
        rate.append(stages.count(i) / sum([x>=i for x in stages]))
    answer = [i+1 for i in sorted(range(len(rate)), key=lambda i: (-rate[i], i))] 
    # 리스트 인덱스에 +1 해서 가져오기. 
    # (-rate[i], i) : rate[i]는 내림차순으로(큰 순서대로) 인덱스 추출하는데, 동일한 값이면 작은 인덱스가 먼저.
    return answer

여기서 시간복잡도 O(MN) (stages : M) 
-> 딕셔너리를 쓰면 시간복잡도 줄어듬!!!
