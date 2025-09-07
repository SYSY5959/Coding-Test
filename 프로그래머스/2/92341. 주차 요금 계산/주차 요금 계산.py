## 혼자 못 품 ㅠㅠㅠ
import math
def minutes(time):  # 시간을 분으로 바꿔주는 함수
    h,m = map(int, time.split(":"))
    return h*60 + m

def solution(fees, records):
    answer = []
    recs = {}   # 딕셔너리 사용!!
    fee = {}
    
    # {차량번호 : [시간, IN/OUT]} 딕셔너리 만들기
    for record in records:
        time, num, io = record.split()
        
        if num in recs:
            recs[num].append([time, io])
        else:
            recs[num] = [[time, io]]
    
    # 주차 요금 계산
    for rec in recs:
        total = 0
        payment = fees[1]
        
        if len(recs[rec])%2 != 0:   # 입차 후 출차 내역 없을 때
            recs[rec].append(["23:59", "OUT"])
            
        for r in recs[rec]:
            if r[1] == "IN":
                total -= minutes(r[0])
            else:
                total += minutes(r[0])
        if total > fees[0]:
            payment += math.ceil((total - fees[0])/fees[2])*fees[3]
            
        fee[rec] = payment
        
    fee = sorted(fee.items())
    print(fee)
    return [f for n,f in fee]