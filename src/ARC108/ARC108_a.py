def run(s, p):
    '''

    '''
    print('Yes' if isinstance(s*p/(p+1), int) else 'No')


if __name__ == '__main__':
    s, p = map(int, input().split())

    run(s,p)