from collections import defaultdict

def run(n, an):
    _an = sorted(list(set(an)))
    d = {}
    l = len(_an)
    for i,e in enumerate(_an):
        d[e] = l-(i+1)
    
    ans = defaultdict(int)
    for e in an:
        ans[d[e]] += 1
    

    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    n = int(input())
    an = list(map(int, input().split()))

    run(n,an)