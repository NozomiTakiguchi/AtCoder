from decorator import trace_perf

@trace_perf
def run(x):
    '''
    5 つの変数 
    x1 , x2 , x3 , x4 , x5
    があります。
    最初、変数 xi には整数 i が代入されていました。
    すぬけくんは、これらの変数の中から 1 つを選んで、その変数に 0 を代入する操作を行いました。
    すぬけくんがこの操作を行ったあとの 5 つの変数の値が与えられます。
    すぬけくんが 0 を代入した変数がどれであったかを答えてください。

    [入力例]
    0 2 3 4 5
    [出力例]
    1
    '''

    for i,v in enumerate(x):
        if v == 0:
            print(i+1)


if __name__ == '__main__':
    x = list(map(int, input().split()))
    run(x)