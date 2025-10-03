
def solution(n, left, right):
    
    # 0~n^2까지 다 만들 필요 없음
    # left~right+1까지만 필요!!! 
    answer = []
    for i in range(left,right+1):
        row = i//n
        col = i%n
        answer.append(max(row,col)+1) 
    
    return answer


# ### 시간 초과
# def solution(n, left, right):
#     answer = []
#     lst = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if lst[i][j] == 0 and i==j:
#                 lst[i][j] = i+1
#             elif lst[i][j] == 0 and i!=j:
#                 lst[i][j] = max(i,j) +1
    
#     answer = sum(lst, [])
#     answer = answer[left:right+1]
    
#     return answer