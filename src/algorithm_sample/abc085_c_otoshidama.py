from decorator import trace_perf

@trace_perf
def run(n, y):
    '''
    10000 円札と、5000 円札と、1000 円札が合計で N 枚あって、合計金額が Y 円であったという。
    このような条件を満たす各金額の札の枚数の組を 1 つ求めなさい。そのような状況が存在し得ない場合には -1 -1 -1 と出力しなさい。

    [制約]
    1≤N≤2000
    1000≤Y≤2∗10^7
    N は整数
    Y は 1000 の倍数
    [数値例]
    N = 9
    Y = 45000
    答え: (4, 0, 5) など
    '''
    # inefficient
    pattern_a = []
    for i in range(n + 1): # 10000 円
        for j in range(n - i + 1): # 5000 円
            for k in range(n - i - j + 1): # 1000 円
                if y == 10000 * i + 5000 * j + 1000 * k and i + j + k == n:
                    pattern_a.append((i, j, k))
    
    # no need to process 3rd loop 
    pattern_b = []
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            if y == 10000 * i + 5000 * j + 1000 * k and i + j + k == n:
                pattern_b.append((i,j,k))

    if len(pattern_a) > 0 and len(pattern_b) > 0:
        print('{}\n{}'.format(pattern_a[0], pattern_b[0]))
    else:
        print('({} {} {})'.format(-1, -1, -1))





if __name__ == '__main__':
    n, y = list(map(int, input().split()))
    run(n, y)