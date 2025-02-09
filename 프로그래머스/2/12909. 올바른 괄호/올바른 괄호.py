def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        else:
            if stack == []:
                answer = False
            else:
                stack.pop()
    if stack != []:
        answer = False

    return answer