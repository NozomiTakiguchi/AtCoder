import itertools
def run(n_m, an_bn):
    '''
    ACL beginner contest C
    Union-Find 木 というのを使って連結成分を取得すれば、連結成分 - 1 が答えになる（らしい）

    '''
    all_cities = [i+1 for i in range(n_m[0])]
    cities = set(list(itertools.chain.from_iterable(an_bn)))
    if n_m[0] - len(cities) <= 0:
        print(0)
    else:
        print(len(set(all_cities)) - len(cities))

if __name__ == '__main__':
    n_m = list(map(int, input().split()))
    an_bn = list(map(int, input().split()) for _ in range(n_m[1]))

    run(n_m, an_bn)
