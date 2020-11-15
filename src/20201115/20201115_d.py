import itertools
def run(n, k, schedule):
    '''

    いもす法というのを使って爆速で計算できるらしい

    '''
    concurrent = [0] * (2*10**5 + 10)
    for i in range(n):
        start_time = schedule[i][0]
        end_time = schedule[i][1]
        amount = schedule[i][2]

        # # これのせいで O(NT) だけの時間がかかってしまう
        # for _i in range(start_time, end_time):
        #     concurrent[_i] += amount
        #     if concurrent[_i] > k:
        #         print('No')
        #         exit()
        
        # 時刻 S になったら水の使用量が amount だけ増える
        concurrent[start_time] += amount
        # これは思いつかん (時刻 T になったら水の使用量が amount だけ「減る」)
        concurrent[end_time] -= amount
    
    for i in range(len(concurrent) - 1):
        # ↑ ですごく時間がかかっていたループをやめて、累積和を利用する（これがいもす法？）
        concurrent[i+1] += concurrent[i]
        if concurrent[i] > k:
            print("No")
            exit()

    print('Yes')
    
    # if len([x for x in concurrent if x > k]) > 0:
    #     print('No')
    # else:
    #     print('Yes')

if __name__ == '__main__':
    n, w = map(int, input().split())
    schedule = [list(map(int, input().split())) for _ in range(n)]
    run(n, w, schedule)