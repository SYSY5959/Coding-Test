def dfs(c):
    global ans
    
    v[c] = 1
    ans += 1
    for n in arr[c]:
        if v[n] == 0:
            dfs(n)
            

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

ans = 0
v = [0]*(n+1)
dfs(1)
print(ans-1)