def dfs(v):
    check[v] = 1
    print(v,end=' ')
    route[v].sort()
    for i in route[v]:
        if not check[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    checkbfs[v] = 1
    while queue:
        w = queue.popleft()
        print(w,end= ' ')
        for i in route[w]:
            if not checkbfs[i]:
                queue.append(i)
                checkbfs[i] = 1

from collections import deque
n,m,v = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(m)]

check = [0]*(n+1)
checkbfs = [0]*(n+1)
route = [[] for _ in range(n+1)]

for i in lst:
    route[i[0]].append(i[1])
    route[i[1]].append(i[0])

dfs(v)
print()
bfs(v)
