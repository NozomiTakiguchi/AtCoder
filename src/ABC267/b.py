from collections import defaultdict


s = input()
l = []
d = defaultdict(list)
d[1].append(int(s[6]))
d[2].append(int(s[3]))
d[3].append(int(s[7]))
d[3].append(int(s[1]))
d[4].append(int(s[4]))
d[4].append(int(s[0]))
d[5].append(int(s[8]))
d[5].append(int(s[2]))
d[6].append(int(s[5]))
d[7].append(int(s[9]))


start = False
split = False
if int(s[0]) == 1:
    print('No')
    exit()

for k,v in d.items():
    if sum(v) > 0:
        start = True
        if split:
            print('Yes')
            exit()
    if sum(v) == 0:
        if start:
            split = True
        start = False

print('No')
    






