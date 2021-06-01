import math

MAX = 100010

def run(l_r):
    '''
    '''
    is_prime = [1]*MAX
    is_prime[0] = 0
    is_prime[1] = 0

    # エラトステネスの篩 -> なんかうまくいっていない
    for i in range(2, MAX):
        if not is_prime[i]:
            continue
        for j in range(i*2, MAX, i):
            is_prime[j] = 0

    #2017 に似た数かどうかを検討
    _2017_like_numbers = [0] * MAX
    for i in range(MAX):
        if i % 2 == 0:
            continue
        if is_prime[i] and is_prime[int((i+1)/2)]:
            _2017_like_numbers[i] = 1
    
    # 累積和を導出
    cumulative_sum = [0] * (MAX+1)
    for i in range(MAX):
        cumulative_sum[i+1] = cumulative_sum[i] + _2017_like_numbers[i]
    
    for e in l_r:
        print(cumulative_sum[e[1]] - cumulative_sum[e[0]-1])
    



if __name__ == '__main__':
    q = int(input())
    l_r = [list(map(int, input().split())) for _ in range(q)]

    run(l_r)