### 내 풀이
def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    
    for num in arr1:
        b = bin(num)[2:]
        if len(b) < n:
            b = "0"*(n - len(b)) + b
        a1.append(b)
        
    for num2 in arr2:
        b2 = bin(num2)[2:]
        if len(b2) < n:
            b2 = "0"*(n - len(b2)) + b2
        a2.append(b2)
        
    for i in range(n):
        s = ""
        for j in range(n): # 하나의 2진수 문자열 안에서 
            if a1[i][j] == "0" and a2[i][j] == "0":
                s += "0"
            elif a1[i][j] == "1" or a2[i][j] == "1":
                s += "1"
        s = s.replace("0", " ")
        s = s.replace("1", "#")
        #print(s)
        answer.append(s)
    
    return answer

### 더 간단한 풀이

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = bin(arr1[i] | arr2[i]) # 그냥 처음부터 or 해서 2진법으로
        num = num[2:].zfill(n) # 예를 들어, 1을 00001로 채워넣기. (공백을 0으로)
        num = num.replace('1', '#').replace('0', ' ')
        answer.append(num)
    return answer
