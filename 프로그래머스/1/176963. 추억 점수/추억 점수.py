def solution(name, yearning, photo):
    answer = []
    dic = {name[i]:yearning[i] for i in range(len(name))}

    for j in range(len(photo)):
        total = 0
        for k in range(len(photo[j])):
            if photo[j][k] in dic:
                total += dic[photo[j][k]]
        answer.append(total)

    return answer