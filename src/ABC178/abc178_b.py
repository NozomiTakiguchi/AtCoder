def run(a, b, c, d):
    '''

    '''
    print(max([a*c, a*d, b*c, b*d]))

if __name__ == '__main__':
    a, b, c, d = list(map(int, input().split()))

    run(a, b, c, d)