def run(x, y, z):
    '''
    see. https://atcoder.jp/contests/abc176/tasks/abc176_a
    '''

    process_time = int(x/y) + 1 if x%y != 0 else int(x/y)
    print(process_time*z)



if __name__ == '__main__':
    x, y, z = list(map(int, input().split()))
    run(x, y, z)