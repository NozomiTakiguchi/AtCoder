def run(n):
    '''

    '''
    # めちゃめちゃ遅い

    # def make_divisors(n):
    #     lower_divisors = []
    #     upper_divisors = []
    #     for i in range(1, int(n**0.5)+1):
    #         if n % i == 0:
    #             lower_divisors.append(i)
    #             if i != n // i:
    #                 upper_divisors.append(n//i)

    #     upper_divisors.reverse()
    #     return lower_divisors + upper_divisors

    # counts = 0
   
    # for i in range(n):
    #     _n = n - (i+1)
    #     if _n == 0:
    #         break
    #     counts += len(make_divisors(_n))
    
    # print(counts)


    # 1 <= A * B <= N-1 になるような A, B の組み合わせを考える
    # B <= (N-1)/A より、A に対して A*B <= N-1 を満たす B は (N-1)/A 個存在する
    counts = 0
    for i in range(1, n):
        counts += (n-1)//i
        print('A = {}, B = {}, C = {}'.format(i, counts, n - (i * counts)))
    print(counts)






if __name__ == '__main__':
    n = int(input())

    run(n)