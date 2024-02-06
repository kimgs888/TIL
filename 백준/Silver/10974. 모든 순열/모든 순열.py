from itertools import permutations
n = int(input())
data = [i for i in range(1,n+1)]
c=list(permutations(data,n))
for num in c:
    print(*num)