string = input()
char = input()
sl = len(string)
cl = len(char)
i = 0
cnt = 0
while i <= sl-cl:
    if string[i:i+cl]==char:
        i = i + cl
        cnt = cnt + 1
        continue
    i = i + 1
print(cnt)