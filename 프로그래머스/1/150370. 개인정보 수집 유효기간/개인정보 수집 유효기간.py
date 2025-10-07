# 문자열 2022.05.19 에 6개월 더하는 함수 
# 보관 가능한 날짜 (언제까지 가능한지)
def date(s, n):
    year,month,day = map(int, s.split('.'))
    month += n
    day -= 1
    if day <= 0:
        month -= 1
        day += 28
    if month > 12:
        year += month//12
        month = month%12
        if month == 0:  # 2021.00.17 == 2020.12.17
            month = 12
            year -=1
    date_string = f'{year}.{month:02d}.{day:02d}'    
    return date_string

def solution(today, terms, privacies):
    answer = []
    
    # 약관 종류 (terms) 딕셔너리 만들기
    dic = {}    
    for term in terms:
        typ, valid = term.split(' ')
        dic[typ] = int(valid)
    
    for i in range(len(privacies)):
        privacy = privacies[i]
        start, what = privacy.split(' ')
        limit = date(start, dic[what])
        print(limit)
        if today > limit:
            answer.append(i+1)
        
    return answer