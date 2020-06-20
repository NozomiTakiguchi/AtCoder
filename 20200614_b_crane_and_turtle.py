from decorator import trace_perf

@trace_perf
def run(x, y):
    '''
    庭に何匹かの動物がいます。これらはそれぞれ、 2 本の足を持つ鶴か 4 本の足を持つ亀のいずれかです。
    高橋くんは、「庭の動物の総数は X 匹で、それらの足の総数は Y 本である」と発言しています。
    この発言が正しいような鶴と亀の数の組合せが存在するか判定してください。

    [入力例]
    3 8
    [出力例]
    Yes
    '''
    for i in range(x + 1): # turtle
        if y == 2 * i + 4 * (x - i):
            print('Yes')
            return
    print('No')



if __name__ == '__main__':
    x, y = list(map(int, input().split()))
    run(x, y)