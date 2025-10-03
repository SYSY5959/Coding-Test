def solution(numbers):
    answer = ''

    lst = sorted(map(str, numbers), key=lambda x:x*3 , reverse = True)
    answer = str(int("".join(lst)))
    return answer