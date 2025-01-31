### 다른 사람 풀이
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]

    #런타임 에러
#    for i in range(len(quiz)):
#        quiz[i] = quiz[i].replace(" ", "")  # 공백 제거
#        x_and_y, z = quiz[i].split("=")  # 좌변과 우변 분리
#        
#        if "+" in x_and_y:
#            x, y = map(int, x_and_y.split("+"))
#            answer.append("O" if x + y == int(z) else "X")
#        elif "-" in x_and_y:
#            x, y = map(int, x_and_y.split("-"))
#            answer.append("O" if x - y == int(z) else "X")
            
    return answer