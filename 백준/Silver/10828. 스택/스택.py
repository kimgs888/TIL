def push1(num):
    ans.append(num)

def pop1():
    if ans:
        print(ans.pop())
    else:
        print(-1)

def size1():
    print(len(ans))

def empty1():
    if len(ans):
        print(0)
    else:
        print(1)

def top1():
    if ans:
        print(ans[-1])
    else:
        print(-1)


n = int(input())
lst = [list(map(str,input().split())) for _ in range(n)]
ans =[]

for i in lst:
    if i[0]=='push':
        push1(int(i[1]))
    elif i[0]=='pop':
        pop1()
    elif i[0]=='empty':
        empty1()
    elif i[0]=='top':
        top1()
    elif i[0]=='size':
        size1()