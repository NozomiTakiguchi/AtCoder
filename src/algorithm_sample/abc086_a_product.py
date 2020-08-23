def run():
    '''
    二つの正整数 a, b が与えられます。 a と b の積が偶数か奇数か判定してください。
    制約:
        1≤a,b≤10000
        a, b は整数
    '''
    _in = list(map(int, input().split()))
    if len(_in) < 2:
        print('invalid input. need 2 values.')
    
    elif _in[0]*_in[1]%2 == 0:
        print('Even')
    else:
        print('Odd')



if __name__ == '__main__':
    run()