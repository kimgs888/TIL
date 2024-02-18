import sys
from collections import deque

di = [1,0,-1,0]
dj = [0,1,0,-1]

def bfs(row,col,lst):
    global num
    q = deque()
    q.append([row,col])
    num = num + 1
    lst[row][col] = num

    while q:
        r,c = q.popleft()
        for i in range(4):
            tmpr = r+di[i]
            tmpc = c+dj[i]
            if 0<=tmpr<n and 0<=tmpc<n and lst[tmpr][tmpc] == 1:
                q.append([tmpr,tmpc])
                lst[tmpr][tmpc] = num

    return

n = int(sys.stdin.readline())
lst = [list(map(int,input())) for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            bfs(i,j,lst)
print(num-1)
ans = []

for j in range(n):
    ans.extend(lst[j])

result = [ans.count(k) for k in range(2,num+1)]
result.sort()

if not result:
    print(0)

a = [print(result[l]) for l in range(num-1)]