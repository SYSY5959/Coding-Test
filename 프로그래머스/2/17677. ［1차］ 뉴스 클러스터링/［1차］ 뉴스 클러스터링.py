import math
from collections import Counter
## 합집합, 교집합 구할 때, 그냥 set 쓰면 중복된 애들 하나로 처리

def make(str1):
    lst = []
    for i in range(len(str1)-1):
        s = str1[i:i+2]
        if s.isalpha():
            lst.append(str.upper(s))
    return lst
def solution(str1, str2):
    answer = 0
    lst1 = make(str1)
    lst2 = make(str2)
    if len(lst1) == 0 and len(lst2) == 0:
        answer = 65536
    else :    
        a = list((Counter(lst1) & Counter(lst2)).elements()) # 교집합
        b = list((Counter(lst1) | Counter(lst2)).elements()) # 합집합
        
        print(a)
        print(b)
        answer = math.floor((len(a)/len(b))*65536)
    
    return answer