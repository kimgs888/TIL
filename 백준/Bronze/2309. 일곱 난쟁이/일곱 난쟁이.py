def height(lst,goal):
    for i in lst:
        for j in lst:
            if i != j and i+j == goal:
                lst.remove(i)
                lst.remove(j)
                return lst

lst = [int(input()) for _ in range(9)]
newlst = height(lst,sum(lst)-100)
newlst.sort()
a = [print(i) for i in newlst]