def run(n):
    '''

    '''

    if n == 1:
        print(0)
    elif n == 2:
        print(2)
    else:
        maxn = 10**n
        counts = maxn - (2*(9**n)) + 8**n
        dividend = (10**9) + 7
        print(counts % dividend)

if __name__ == '__main__':
    n = int(input())

    run(n)