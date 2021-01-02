def run(n, _list):
    '''
    '''
    sorted_list = sorted(_list, key=lambda e: (e[0]*2 + e[1]), reverse=True)
    cnt = 0 
    vt = 0 # 高橋さんの得票数. インクリメントする
    va = sum(e[0] for e in sorted_list) # 青木さんの得票数. デクリメントする
    if va <= max([sum(e) for e in sorted_list]):
        print(1)
        exit()

    for e in sorted_list:
        cnt += 1
        va -= e[0]
        vt += sum(e)
        if vt > va:
            print(cnt)
            exit()


if __name__ == '__main__':
    n = int(input())
    _list = [list(map(int, input().split())) for _ in range(n)]

    run(n, _list)