import math
def lcm(a,b):
    ans = (a*b)//(math.gcd(a,b))
    return ans
def solution(arr):
    answer = lcm(arr[0],arr[1])
    for i in range(2,len(arr)):
        answer = lcm(arr[i], answer)
        
    return answer