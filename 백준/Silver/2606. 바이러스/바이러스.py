def dfs(i,net,check):
    check[i] = True
    # print(i)

    for j in net[i]:
        if not check[j]:
            dfs(j,net,check)


num = int(input())
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

net = [[] for _ in range(num+1)]
for i in lst:
    net[i[0]].append(i[1])
    net[i[1]].append(i[0])

check = [False]*(num+1)

v = 1

dfs(v,net,check)

print(sum(check)-1)