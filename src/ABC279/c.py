from collections import defaultdict
def main(h,w,ds,dt):
    dsl = sorted(list(ds.values()))
    dtl = sorted(list(dt.values()))

    ans = 'Yes'
    for dse,dte in zip(dsl,dtl):
        if dse == dte:
            continue
        else:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    h,w = map(int, input().split())
    ds = defaultdict(list)
    dt = defaultdict(list)
    for _ in range(h):
        for j,s in enumerate(input()):
            ds[j].append(s)

    for _ in range(h):
        for j,s in enumerate(input()):
            dt[j].append(s)
    
    main(h,w,ds,dt)
    