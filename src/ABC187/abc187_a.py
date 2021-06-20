def run(a, b):
    '''

    '''
    sa = sum([int(i) for i in str(a)])
    sb = sum([int(i) for i in str(b)])
    print(sa if sa >= sb else sb)



if __name__ == '__main__':
    a, b = map(int, input().split())

    run(a,b)