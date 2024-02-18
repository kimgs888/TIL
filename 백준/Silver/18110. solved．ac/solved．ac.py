import sys
n = int(sys.stdin.readline().strip())
EPS = 1e-9

lst = [int(sys.stdin.readline().strip()) for _ in range(n)]
if n ==0:
    print(0)
elif n:
    limit = round(n*0.15+EPS)
    lst.sort()
    ans = 0
    div = 0
    for i in range(limit,n-limit):
        ans = ans + lst[i]
        div = div + 1

    print(round((ans/div)+EPS))