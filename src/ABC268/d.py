import itertools

def run(n,m,s,t):
    l = list(itertools.permutations(s))
    pass


if __name__ == '__main__':
    n,m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    t = []
    for i in range(m):
        t.append(input())

    run(n,m,s,t)