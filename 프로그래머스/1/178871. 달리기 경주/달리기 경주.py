### 시간 초과 : players.index(name) 에서 계산복잡도 O(players * callings)
# def solution(players, callings):
#     for name in callings:
#         i = players.index(name)
#         players[i], players[i-1] = players[i-1], players[i]
#     return players

def solution(players, callings):
    dic = {p:i for i,p in enumerate(players)}
    
    for name in callings:
        i = dic[name]
        
        # 딕셔너리에서 선수 인덱스 바꿔주기
        dic[name] = i-1
        dic[players[i-1]] = i
        
        # 자리 스위치
        players[i], players[i-1] = players[i-1], players[i]
        
        
        
    return players