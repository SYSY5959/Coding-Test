## 혼자 못 품ㅠㅠ 
def solution(want, number, discount):
    answer = 0
    shop = []
    
    for i in range(len(want)):
        for j in range(number[i]):
            shop.append(want[i])
    shop.sort()
    for i in range(len(discount)-9): # 리스트 요소 10개 되는 애들만 확인하면 됨
        dlist = discount[i:i+10]
        dlist.sort()
        if dlist == shop:
            answer += 1
        
    
    return answer