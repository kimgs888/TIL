import sys
for t in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ans = n
    if ans < 2:
        print(2)
        continue
    findN = 1
    while 1:
        for i in range(2,int(ans**0.5)+1):
            if ans%i == 0:
                break
        else:
            findN = 0

        if not findN:
            break

        ans = ans + 1

    print(ans)