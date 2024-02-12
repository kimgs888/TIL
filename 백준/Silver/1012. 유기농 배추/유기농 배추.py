import sys
sys.setrecursionlimit(10**7)
def dfs(r,c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return False

    if lst[r][c]:
        lst[r][c] = 0
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
        return True

    return False

for t in range(int(input())):
    m,n,k = map(int,input().split()) # 열 m,c / 행 n,r
    lst = [[0]*m for _ in range(n)]

    for i in range(k):
        c,r = map(int,input().split())
        lst[r][c] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                cnt = cnt + 1

    print(cnt)