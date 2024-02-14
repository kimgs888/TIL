lst = input()
char = lst.upper()
check = set(char)
ans = []
fn = 0
for i in check:
    num = char.count(i)
    if fn<num:
        ans = [i]
        fn = num
    elif fn == num:
        ans.append(i)

if len(ans)>1:
    print('?')
elif len(ans):
    print(*ans)
