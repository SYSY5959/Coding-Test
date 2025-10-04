def solution(elements):
    answer = 0
    total = set()

    for i in range(1,len(elements)+1):
        lst = elements + elements[:i-1]
        for j in range(len(elements)):
            total.add(sum(lst[j:j+i]))
    answer = len(total)
    return answer