def run(n, _n):
    '''

    '''
    def make_divisors(n):
        lower_divisors , upper_divisors = [], []
        i = 1
        while i*i <= n:
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n//i)
            i += 1
        return lower_divisors + upper_divisors[::-1]
    max_num = 0
    for n in _n[::-1]:
        if len([elm for elm in _n if elm%n == 0]) > 1:
            max_num = n
            break
    else:
        max_num = max(_n)

    divsors = make_divisors(max_num)
    _tmp = 0
    ans = 0
    for e in divsors[::-1]:
        _ans = len([num for num in _n if num % e == 0])
        # print('e: {} / _ans: {}'.format(e, _ans))
        if _ans > _tmp and e >= 2:
            _tmp = _ans
            ans = e
    
    print(ans)



if __name__ == '__main__':
    n = int(input())
    _n = list(map(int, input().split()))
    run(n, _n)