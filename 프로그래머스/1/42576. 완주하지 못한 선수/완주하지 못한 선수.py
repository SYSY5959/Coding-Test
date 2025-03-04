from collections import Counter
def name(people):
    dic = Counter(people)
    name_list = []
    val = list(dic.values())
    key = list(dic.keys())

    for key,val in dic.items():
        for j in range(val):
            name_list.append(key+'_'+str(j))
    return name_list

def solution(participant, completion):
    lst1 = name(participant)
    lst2 = name(completion)
    
    lst = set(lst1) - set(lst2)
    ans = ''.join(lst)
    ans = ans.split("_")[0]       
    return ans