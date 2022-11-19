n = int(input())
ans = 'Yes'
sn = []

for _ in range(n):
    sn.append(input())


for s in sn:
    if s[0] not in ['H', 'D','C','S']:
        ans = 'No'
        break
    if s[1] not in ['A','2','3','4','5','6','7','8','9','T','J','Q','K']:
        ans = 'No'
        break

if len(sn) != len(list(set(sn))):
    ans = 'No'

print(ans)