def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    dic = {"code":0, "date":1, "maximum":2, "remain":3}
    ext2 = dic[ext]
    sort2 = dic[sort_by]
    
    for d in data:
        if d[ext2] < val_ext:
            answer.append(d)
    answer.remove([])
    
    # lst.sort(key=lambda x:x[0]) -> 리스트 원본을 정렬
    # sorted(lst, key=lambda x:x[0])
    answer = sorted(answer, key=lambda x: x[sort2])

    return answer