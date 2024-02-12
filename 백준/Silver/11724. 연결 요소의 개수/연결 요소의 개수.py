def dfs(v):
    check[v] = 1
    for i in route[v]:
        if not check[i]:
            dfs(i)

import sys
sys.setrecursionlimit(10**7)
m,n = map(int,sys.stdin.readline().split())
check = [0] * (m+1)
route = [[] for _ in range(m+1)]
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in lst:
    route[i[0]].append(i[1])
    route[i[1]].append(i[0])

cnt = 0
for i in range(1,m+1):
    if not check[i]:
        dfs(i)
        cnt = cnt + 1


print(cnt)