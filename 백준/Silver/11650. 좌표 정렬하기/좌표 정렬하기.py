import sys
n = int(sys.stdin.readline().strip())
lst = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
lst.sort()
for i in lst:
    print(*i)