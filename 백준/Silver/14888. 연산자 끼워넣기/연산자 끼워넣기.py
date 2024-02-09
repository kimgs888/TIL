def compute(comp):
    result = lst[0]

    for i in range(N-1):
        if comp[i] == 0:
            result = result + lst[i+1]
        elif comp[i] == 1:
            result = result - lst[i+1]
        elif comp[i] == 2:
            result = result * lst[i+1]
        elif comp[i] == 3:

            if result < 0:
                result = -(abs(result)//lst[i+1])
            else:
                result = result//lst[i+1]

    return result

from itertools import permutations

N = int(input())
lst = list(map(int,input().split()))
compTemp = list(map(int,input().split()))

comp = [i for i in range(len(compTemp)) for j in range(compTemp[i])]
ans = []
compComb = set(permutations(comp,N-1))
for cal in compComb:
    ans.append(compute(cal))


print(max(ans))
print(min(ans))