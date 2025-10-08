from itertools import permutations

def check(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
    
def solution(numbers):
    answer = 0
    unique = set()
    for i in range(1, len(numbers)+1):
        # numbers로 만들 수 있는 i 길이의 모든 순열 구하기
        p_list = permutations(list(numbers), i)
        # p_list
        # i = 1 : ('1'), ('7')
        # i = 2 : ('1', '7'), ('7', '1') 
        for p in p_list:
            unique.add(int("".join(p)))
    
    # 만들어진 숫자들이 소수인지 판단
    for n in unique:
        if check(n) == True:
            answer+=1

    return answer