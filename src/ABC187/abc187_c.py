def run(n, sn):
    '''

    '''
    list_without_preffix = set([e for e in sn if not e.startswith('!')])
    others = set([e[1::] for e in set(sn) - list_without_preffix])
    ans = list_without_preffix & others
    print('satisfiable' if len(ans) == 0 else list(ans)[0])

if __name__ == '__main__':
    n = int(input())
    sn = list(input() for _ in range(n))
    run(n, sn)