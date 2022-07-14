def run(n,q,s,queries):
    s_dict = {}
    for idx, c in enumerate(s):
        s_dict[idx] = c
    
    rotation = 0
    ans = []
    for e in queries:
        query, cnt = e
        if query == 1:
            rotation += cnt
        if query == 2:
            ans.append((cnt-1-rotation)%n)
    
    for idx in ans:
        print(s_dict[idx])


if __name__ == '__main__':
    n,q = map(int, input().split())
    s = input()
    queries = [list(map(int, input().split())) for _ in range(q)]

    run(n,q,s,queries)