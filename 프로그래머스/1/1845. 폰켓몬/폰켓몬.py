from collections import Counter
def solution(nums):
    answer = 0
    dic = Counter(nums) # len(dic) 포켓몬 종류 개수
    get = len(nums)//2 # 가질 수 있는 포켓몬 개수
    if get >= len(dic):
        answer = len(dic)
    else:
        answer = get
    return answer