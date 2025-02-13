def solution(s, n):
    answer = []

    for c in s:
        if c.isupper():  # 대문자인 경우
            answer.append(chr((ord(c) - ord('A') + n) % 26 + ord('A')))
        elif c.islower():  # 소문자인 경우
            answer.append(chr((ord(c) - ord('a') + n) % 26 + ord('a')))
        else:  # 공백 처리
            answer.append(" ")

    return "".join(answer)
