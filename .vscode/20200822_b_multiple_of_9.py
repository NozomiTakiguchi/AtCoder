def run(x):
    '''
    see. https://atcoder.jp/contests/abc176/tasks/abc176_b
    '''

    # sum = 0
    # while x > 0:
    #     sum += x%10
    #     x = int(x/10)

    # print('Yes' if sum % 9 == 0 else 'No')
    print('Yes' if x % 9 == 0 else 'No')


if __name__ == '__main__':
    x = int(input())
    run(x)