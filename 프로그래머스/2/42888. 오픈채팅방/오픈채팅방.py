def solution(record):
    answer = []
    dic = {}
    for s in record:
        rec = s.split(" ")
        act,uid = rec[0],rec[1]
        if act=='Enter' or act=='Change':
            name = rec[2]
            dic[uid] = name
    for s2 in record:
        rec2 = s2.split(" ")
        act2,id2 = rec2[0],rec2[1]
        if act2 == "Enter":
            answer.append(dic[id2]+"님이 들어왔습니다.")
        if act2 == "Leave":
            answer.append(dic[id2] + "님이 나갔습니다.")
    
    return answer