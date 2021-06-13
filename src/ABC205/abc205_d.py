# 二分探索でいけそうって思った。。。
# 実際それで解いてるっぽい。。悔しい。
def run(n, q):

    a = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        queries.append(int(input()))
    
    ans = 0
    _len = len(a)
    for i in queries:
        _extlen = len([j for j in a if i >= j])
        if _extlen == 0:
            print(i)
            continue
        print(i + _extlen + (_len - _extlen))
        

if __name__ == '__main__':
    n, q = map(int, input().split())
    run(n, q)