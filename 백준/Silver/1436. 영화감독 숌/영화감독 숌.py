N = int(input())
num =666
cnt = 0
while 1:
    tmpNum = str(num)
    if '666' in tmpNum:
        cnt = cnt + 1
    if N == cnt:
        print(num)
        break
    num = num + 1