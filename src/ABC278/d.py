from collections import defaultdict

def main(n,a,_q,query):

    d = defaultdict(int)
    default = 0
    for q in query:
        if q[0] == 3:
            print((a[q[1]-1] if default==0 else default)+d[q[1]])
        elif q[0] == 2:
            _idx, point = q[1:]
            d[_idx] += point
        else:
            default = q[1]
            d = defaultdict(int)
    pass

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))

    main(n,a,q,query)