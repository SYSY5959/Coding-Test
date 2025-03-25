def day(n):
    if n % 7 == 0:
        ans = 'FRI'
    elif n % 7 == 1:
        ans = 'SAT'
    elif n % 7 == 2:
        ans = 'SUN'
    elif n % 7 == 3:
        ans = 'MON'
    elif n % 7 == 4:
        ans = 'TUE'
    elif n % 7 == 5:
        ans = 'WED'
    elif n % 7 == 6:
        ans = 'THU'
    
    return ans

def solution(a, b):
    dic = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    date = sum(dic[k] for k in range(1,a)) + b
    n = date - 1
    answer = day(n)
    return answer