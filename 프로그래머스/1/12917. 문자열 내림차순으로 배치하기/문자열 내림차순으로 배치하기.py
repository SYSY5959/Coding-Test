def solution(s):
    answer = ''
    lst = list(s)
    lst.sort(reverse=True)
    answer = "".join(lst)
    return answer