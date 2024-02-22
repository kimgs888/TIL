import sys
n,k = map(int,sys.stdin.readline().strip().split())
lst = list(map(int,sys.stdin.readline().strip()))
stack = []
cnt = k
for i in range(n):
    while(cnt>0 and stack and stack[-1] < lst[i]):
        stack.pop()
        cnt = cnt - 1
    stack.append(lst[i])
print(''.join(list(map(str,stack[:n-k]))))