def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]
    lst2 = ["ayaaya", "yeye", "woowoo", "mama"]
    for b in babbling:
        # 가장 먼저 연속한 단어들은 제거하고 시작
        if any(char in b for char in lst2):
            continue
            
        # lst안에 있는 원소들 있으면, 다 삭제하고(공백으로 대체)
        for l in lst:
            b = b.replace(l," ")
        # 최종 문자열이 공백 제거 후에 ''이면 발음할 수 있는 단어
        if len(b.strip())==0:
            answer +=1   
            
    return answer