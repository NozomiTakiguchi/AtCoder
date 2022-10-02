from collections import defaultdict
MAX = 3*(10**5)

def run(n,a):
    a = sorted(a)
    d = defaultdict(int)

    for e in a:
        d[e] += 1

    cnt = n
    ans = 0
    for i in range(n):
        v = d[i+1]
        if v != 0:
            if cnt <= 0:
                break
            cnt = cnt-1
        else:
            if cnt < 2:
                break
            cnt = cnt -2
        ans = ans+1
    print(ans)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    run(n,a)