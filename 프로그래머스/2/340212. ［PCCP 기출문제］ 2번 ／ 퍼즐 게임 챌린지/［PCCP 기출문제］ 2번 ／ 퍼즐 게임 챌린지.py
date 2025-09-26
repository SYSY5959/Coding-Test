### 이분 탐색 (Binary Search)
def tot(level, diffs, times):
    total = 0
    for i in range(len(diffs)):
        if level >= diffs[i]:
            total += times[i]
        else:
            if i == 0:
                total += (diffs[i]-level)*times[i]+times[i]
            total += (diffs[i]-level)*(times[i-1]+times[i])+times[i]
    return total

def solution(diffs,times,limit):
    answer = 0
    ## 1. 탐색 범위 설정
    left = min(diffs) # 최소 level
    right = max(diffs)+1 # 가능한 최대 level + 1 (문제 조건에 따라 설정)
    
    ## 2. 이분 탐색 시작 -> 주로 while 문 사용
    while left <= right:
        mid = (left + right) // 2 # 중간 level로 후보 결정 (이분 탐색)
        
        ## 3. 해당 level로 시간 계산
        total = tot(mid,diffs,times)
        
        ## 4. 범위 좁히기
        if total <= limit:
            # 성공 ! -> 더 낮은 level 가능한지 확인
            answer = mid
            right = mid -1
        else:
            # 실패 -> level 더 높이기
            left = mid + 1
    return answer
    
## 시간 초과

# def tot(level, diffs, times):
#     total = 0
#     for i in range(len(diffs)):
#         if level >= diffs[i]:
#             total += times[i]
#         else:
#             total += (diffs[i]-level)*(times[i-1]+times[i])+times[i]
#     return total

# def solution(diffs, times, limit):
#     answer = 0
#     level = min(diffs) # 1
    
#     for i in range(level,max(diffs)+1):
#         total = tot(level, diffs, times)
#         level += 1
#         if total <= limit:
#             answer = level-1
#             break
        
#     return answer