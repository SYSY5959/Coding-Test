import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        # 큰 원 안쪽의 최대 y (경계 포함)
        y_max = math.floor(abs(r2**2 - x**2) ** 0.5)
        if x >= r1+1:
            y_min = 0
        else:
            # 작은 원 바깥의 최소 y (경계 제외)
            y_min = math.ceil(abs(r1**2 - x**2) ** 0.5)
        answer += (y_max - y_min + 1)
    return answer * 4