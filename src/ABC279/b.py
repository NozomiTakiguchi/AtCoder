s = input()
t = input()


if len(s) < len(t):
    print('No')
    exit()

tlen = len(t)
for i in range(len(s)-tlen+1):
    if t == s[i:i+tlen]:
        print('Yes')
        exit()

print('No')