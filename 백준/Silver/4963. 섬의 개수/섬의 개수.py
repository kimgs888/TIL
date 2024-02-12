import sys
sys.setrecursionlimit(10**7)

def dfs(r,c):
    if r < 0 or r >= h or c < 0 or c >= w:
        return False

    if lst[r][c]:
        lst[r][c] = 0
        dfs(r+1,c)
        dfs(r+1,c+1)
        dfs(r,c+1)
        dfs(r-1,c+1)
        dfs(r-1,c)
        dfs(r-1,c-1)
        dfs(r,c-1)
        dfs(r+1,c-1)
        return True

    return False


while 1:
    w,h = map(int,sys.stdin.readline().split())

    if not w:
        break

    lst = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if lst[i][j]:
                dfs(i,j)
                cnt = cnt + 1

    print(cnt)