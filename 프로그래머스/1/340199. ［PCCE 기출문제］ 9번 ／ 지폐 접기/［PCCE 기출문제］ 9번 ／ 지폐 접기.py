import math
def solution(wallet, bill):
    answer = 0
    while (min(wallet) < min(bill)) or (max(wallet) < max(bill)):
        answer += 1
        maxindex = bill.index(max(bill))
        bill[maxindex] = math.floor(bill[maxindex] / 2)
    return answer