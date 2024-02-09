n = int(input())
lst = list(map(int,input().split()))

lst.sort(reverse=1)
result = 0

if n%2 ==0:

    half = int(n/2)-1
    result = result + lst[half]
    result = result - lst[(half)+1]

    for i in range((half)):
        result = result + (lst[i]*2)
        result = result - (lst[(n-1)-i]*2)

else:

    half = int(n // 2)

    for i in range((half)):
        result = result + (lst[i]*2)
        result = result - (lst[(n-1)-i]*2)

    if abs(lst[half]-lst[half+1]) > abs(lst[half]-lst[half-1]):
        result = result - (lst[half-1])
        result = result + (lst[half])
    else:
        result = result + (lst[half+1])
        result = result - (lst[half])

print(result)