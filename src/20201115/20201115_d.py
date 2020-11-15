import itertools
def run(n, k, schedule):
    '''

    いもす法というのを使って爆速で計算できるらしい

    '''
    # 一番遅くまで使う予定がある人を先頭にした
    concurrent_users = [0] * 2*10**5
    for i in range(n):
        start_time = schedule[i][0]
        end_time = schedule[i][1]
        amount = schedule[i][2]
        amount_list = [amount] * (end_time - start_time)

        for _i in range(start_time, end_time):
            concurrent_users[_i] += amount
            if concurrent_users[_i] > k:
                print('No')
                exit()
    print('Yes')
    
    # if len([x for x in concurrent_users if x > k]) > 0:
    #     print('No')
    # else:
    #     print('Yes')






if __name__ == '__main__':
    n, w = map(int, input().split())
    schedule = [list(map(int, input().split())) for _ in range(n)]
    run(n, w, schedule)