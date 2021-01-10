import decimal
import math
def run(n, m):
    '''

    '''
    if n > m:
        print('Yes' if m+3 > n else 'No')
    else:
        print('Yes' if n+3 > m else 'No')




if __name__ == '__main__':
    n, m = map(int, input().split())

    run(n,m)