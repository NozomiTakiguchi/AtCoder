import itertools
def run(n, a, b):
    '''

    '''
    ans = 0
    for i, j in zip(a, b):
        ans += i*j
    print('Yes' if ans == 0 else 'No')

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    run(n, a, b)