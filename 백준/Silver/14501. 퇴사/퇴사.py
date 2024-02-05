n = int(input())
dp = [0]*(n+1)
lst = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    t = lst[i][0]
    p = lst[i][1]

    if i+t>n:
        continue
    else:
        dp[i] = max(dp[:i+1])
        dp[i+t] = max(dp[i]+p,dp[i+t])
result = max(dp)
print(result)