def run(n, s_list):
    s_list = [[idx, e] for idx, e in enumerate(s_list)]
    sorted_list = sorted(s_list, key=lambda e:e[1])

    cnt = 1
    prev = ''
    ans = []
    for i in sorted_list:
        s = i[1]
        if prev == s:
            ans.append([i[0], f'{s}({cnt})'])
            cnt += 1
        else:
            ans.append([i[0],s])
            cnt = 1
            prev = s
    
    ans = sorted(ans, key=lambda e:e[0])
    for e in ans:
        print(e[1])



if __name__ == '__main__':
    n = int(input())
    s_list = [input() for _ in range(n)]
    run(n, s_list)