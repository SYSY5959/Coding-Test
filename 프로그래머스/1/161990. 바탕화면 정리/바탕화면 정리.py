def solution(wallpaper):
    answer = []
    row = []
    col = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                row.append(i)
                col.append(j)
    if len(row) == 1 and len(col) == 1:
        answer = [row[0],col[0],row[0]+1,col[0]+1]
    else:
        answer.append(min(row))
        answer.append(min(col))
        answer.append(max(row)+1)
        answer.append(max(col)+1)
    
    return answer