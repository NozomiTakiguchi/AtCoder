
def run(n, k, _l):
    friends = sorted(_l, key=lambda x: x[0])
    point_and_amount = {}
    for f in friends:
        if str(f[0]) in point_and_amount:
            point_and_amount[str(f[0])] += f[1]
        else:
            point_and_amount[str(f[0])] = f[1]
    
    amount = k
    prev = 0
    for p, a  in point_and_amount.items():
        p = int(p)
        if amount < (p - prev):
            prev += amount
            print(prev)
            exit()
        amount -= (p - prev)
        amount += a
        prev = p
    print(prev+amount)

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    
    _l = [list(map(int, input().split())) for _ in range(n)]

    run(n, k, _l)