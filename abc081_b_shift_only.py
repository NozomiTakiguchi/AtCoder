def run():
    '''
    黒板に NN 個の正の整数 A1,…,AN が書かれています。
    すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます。
    黒板に書かれている整数全てを 2 で割ったものに置き換える
    すぬけ君は最大で何回操作を行うことができるかを求めてください。
    [制約]
    1 <= N <= 200
    1 <= Ai <= 10^9
    '''
    _in = list(map(int, input().split()))
    count = 0
    while True:
        if len([i for i in _in if i%2 != 0]) > 0:
            print('maximum trial number is {}'.format(count))
            break
        if 0 in _in:
            print('maximum trial number is {},'.format(count))
            break
        _in = [int(i/2) for i in _in]
        count += 1


if __name__ == '__main__':
    run()