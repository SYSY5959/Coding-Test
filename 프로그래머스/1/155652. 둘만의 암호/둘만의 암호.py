def solution(s, skip, index):
    answer = ''
    skip_set = set(skip)  # 문자열에서 체크할 문자들을 빠르게 확인하기 위해 set 사용
    
    for l in s:
        count = 0
        new_char = l
        while count < index:
            # 다음 문자로 이동
            new_char = chr((ord(new_char) - ord('a') + 1) % 26 + ord('a'))  
            if new_char not in skip_set:  # skip에 없는 문자만 count 증가
                count += 1
        answer += new_char
    
    return answer