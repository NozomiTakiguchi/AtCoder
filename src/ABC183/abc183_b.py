def run(a, b, c, d):
    '''

    '''
    counter_point = -1*b #y 座標

    x = a - counter_point*((c - a)/(d - counter_point))
    print(x)



if __name__ == '__main__':
    a, b, c, d= map(int, input().split())

    run(a,b,c,d)