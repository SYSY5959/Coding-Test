def dfs(index, sm, cnt):
    global ans
    if index == N:
        if sm == S and cnt > 0:
            ans += 1
        return 
    dfs(index+1, sm+arr[index], cnt+1)
    dfs(index+1, sm, cnt)
    
N,S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
dfs(0,0,0)
print(ans)