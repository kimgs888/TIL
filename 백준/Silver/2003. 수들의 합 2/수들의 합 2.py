n,m = map(int,input().split())
lst = list(map(int,input().split()))
newlst = lst
cnt = 0
for i in range(n):
    cnt = cnt + lst.count(m)
    newlst=newlst[1:]
    lst = [x + y for x, y in zip(lst, newlst)]
print(cnt)