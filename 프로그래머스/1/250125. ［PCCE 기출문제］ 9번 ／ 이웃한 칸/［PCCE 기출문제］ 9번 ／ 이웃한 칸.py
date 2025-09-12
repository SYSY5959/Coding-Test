def solution(board, h, w):
    answer = 0
    n = len(board)
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]

    for i in range(4):
        ch, cw = h+dh[i], w+dw[i]
        if 0<=ch<n and 0<=cw<n and board[h][w] == board[ch][cw]:
            answer +=1
    return answer