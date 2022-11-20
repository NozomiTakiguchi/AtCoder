from collections import defaultdict

def main(n,q,tab):
    d = defaultdict(lambda:defaultdict(bool))
    for e in tab:
        t,a,b = e
        if t == 1:
            d[a][b] = True
        elif t == 2:
            d[a][b] = False
        else:
            if d[a][b] and d[b][a]:
                print('Yes')
            else:
                print('No')


if __name__ == '__main__':
    n,q = map(int, input().split())
    tab = []
    for _ in range(q):
        tab.append(list(map(int, input().split())))
    main(n,q,tab)