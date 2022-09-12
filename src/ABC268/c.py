'''
e.g
0 ~ 9 が時計回りに円に並んでいるとき、
[1] 2 から時計回りに 6 までの距離は??? → (6-2)mod10 = 4
[2] 3 から時計回りに 1 までの距離は??? → (1-3)mod10 = 7
→ 前も思ったけど、円に並んでる、とか、末尾を先頭に、とかでは「余りの考え方」を使う
'''

from collections import defaultdict
def run(n,p):
    d = defaultdict(int)

    for i,e in enumerate(p):
        t = (e-i)%n
        d[(t-1)%n]+=1
        d[t%n]+=1
        d[(t+1)%n]+=1

    ans = []
    for v in d.values():
        ans.append(v)
    print(max(ans))


if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    run(n,p)
