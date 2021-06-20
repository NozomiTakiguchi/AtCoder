import itertools
def run(a, b, c):
    '''

    いもす法というのを使って爆速で計算できるらしい

    '''
    print((100-a)*(a/(a+b+c))+(100-b)*(b/(a+b+c))+(100-c)*(c/(a+b+c)))


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    run(a, b, c)