n = int(input())
arr = list(map(int, input().split()))
# LIS 알고리즘의 반대여서..
arr.reverse()

# 만들 수 있는 수열의 최소 길이는 1이니까
d = [1]*n

# LIS 알고리즘 수행
for i in range(n): # 모든 수열 다 확인
    for j in range(0,i): # 현재 수 앞부분까지 다시 확인
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j]+1)

print(n - max(d))