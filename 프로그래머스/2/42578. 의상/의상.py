def solution(clothes):
    dic = {}
    for cloth in clothes:
        name = cloth[0]
        typ = cloth[1]
        if typ not in list(dic.keys()):
            dic[typ] = [name]
        else:
            dic[typ].append(name)
    
    cnt = [] # 옷 종류별로 몇개인지 저장하는 리스트
    for key,value in dic.items():
        cnt.append(len(value))
        
    answer = 1
    for c in cnt:
        answer *= (c+1)

    return answer-1