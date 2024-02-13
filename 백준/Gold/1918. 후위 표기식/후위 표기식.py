import sys
lst = (sys.stdin.readline())
comp = list('('+lst+')')
isp = {'(': 0,'*': 2,'/': 2,'+':1,'-':1,')':-1}
icp = {'(': 3,'*': 2,'/': 2,'+':1,'-':1,')':-1}

ans = ''
stack = []

for i in comp:
    if i.isalpha():
        ans = ans + i
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while 1:
                cal = stack.pop()
                if cal =='(':
                    break
                ans = ans + cal
        elif i in '*/-+' and isp[stack[-1]]<icp[i]:
            stack.append(i)
        elif i in '*/-+' and isp[stack[-1]] >= icp[i]:
            while 1:
                if isp[stack[-1]] < icp[i]:
                    break
                cal = stack.pop()
                ans = ans + cal
            stack.append(i)

print(ans)