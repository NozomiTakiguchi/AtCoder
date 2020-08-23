import time
def run():
    '''
    500 円玉を A 枚、 100 円玉を B 枚、 50 円玉を C 枚持っています。これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りあるでしょうか ?
    [制約]
    0≤A,B,C≤50
    A+B+C≥1
    50≤X≤20000
    A,B,C は整数である
    X は 50 の倍数である
    '''
    _in = [int(input()) for _ in range(4)]
    s_time = time.time()
    x = _in.pop(-1)

    a = _in[0] # 500 円玉の枚数
    b = _in[1] # 100 円玉の枚数
    c = _in[2] # 50 円玉の枚数

    count = 0
    for i1 in range(a):
        for i2 in range(b):
            for i3 in range(c):
                if x == i1*500 + i2*100 + i3*50:
                    count += 1

    print('There {} {} {}. process latency=[{}]'.format('is' if count == 1 else 'are', count, 'way' if count == 1 else 'ways', time.time() - s_time))





if __name__ == '__main__':
    run()