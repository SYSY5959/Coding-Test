### 그리디 알고리즘
def solution(n, m, section):
    answer = 0
    paint_end = 0  # 지금까지 칠해진 마지막 위치
    
    for s in section:
        if s > paint_end:
            answer += 1
            paint_end = s + m - 1
    return answer



## 이렇게 풀면, 중간에 칠할 필요 없는 구간을 고려하지 않음. 연속되어 있을 때만 정답이 됨
# import math
# def solution(n, m, section):
#     answer = 0
#     ran = max(section)-min(section)+1
#     if ran <= m:
#         answer = 1
#     answer = math.ceil(ran/m)
#     return answer