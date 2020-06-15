import time
def run():
    '''
    1 以上 N 以下の整数のうち、10 進法で各桁の和が A 以上 B 以下であるものについて、総和を求めてください
    [制約]
    1≤N≤10^4
    1≤A≤B≤36
    入力はすべて整数
    '''
    # このやり方が可能なのは 10 進数のときだけ？
    n, a, b = [int(input()) for _ in range(3)]

    num_sum = 0
    for v in range(n):
        _digits = list(str(v+1))
        _val = sum(int(i) for i in _digits)
        if _val >= a and _val <= b:
            num_sum += v+1
    print('====')
    print(num_sum)

    # 2 進数でもできる
    def _sum_of_digits(num):
        num_sum = 0
        while num > 0:
            num_sum += num % 10
            num = int(num/10)
        return num_sum

    total = 0
    for v in range(n):
        _sum = _sum_of_digits(v+1)
        if _sum >= a and _sum <= b:
            total += v+1

    print(total)

if __name__ == '__main__':
    run()