def solution(number, k):
    stack = []  # 맨 앞자리수 크게 만들기 위해..
    
    for n in number:
        while stack and k>0 and stack[-1]<n:   # 앞자리 수 < 뒷자리수
            stack.pop()
            k -= 1
        stack.append(n)
    if k!= 0:
        return number[:-k]
    else:
        return "".join(stack)
            
        
    return answer