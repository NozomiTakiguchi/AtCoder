import time
def run(n, seq, num, trials):
    '''
    あなたは、 N 個の正整数 A1 , A2 , ⋯ , AN からなる数列 A を持っています。 
    あなたは、これから以下の操作を Q 回、続けて行います。 
    i 回目の操作では、値が Bi である要素すべてを Ci に置き換えます。 すべての 
    i ( 1 ≤ i ≤ Q) に対して、 i 回目の操作が行われた後の数列 A のすべての要素の和、 Si を求めてください。

    [制約]
    入力は全て整数
    1 ≤ N ,Q ,Ai ,Bi ,Ci ≤ 10^5 
    Bi ≠ Ci

    [入力例]
    4
    1 2 3 4
    3
    1 2
    3 4
    2 4
    
    [出力例]
    11
    12
    16
    '''

    #  TODO 下全部 LTE で不正解

    # count_dict = {i+1 : seq.count(i+1) for i in range(100000)}
    # count_list = [seq.count(i+1) for i in range(100000)]
    # count_list = [0 if i+1 not in seq else seq.count(i + 1) for i in range(100000)]
    # count_list = [count_list[i-1] if i not in seq or count_list[i-1] != 0 else seq.count(i) for i in seq]

    count_list = [0] * 100000
    for i in seq:
        count_list[i-1] = count_list[i-1] if count_list[i-1] != 0 else seq.count(i)
    
    # count_list = []
    # for i in range(100000):
    #     count_list.append(0 if i+1 not in seq else seq.count(i+1))

    _sum = sum((k+1)*v for k,v in enumerate(count_list))
    for i in range(num):
        b, c = trials[i]
        _val = count_list[b-1]
        if _val == 0:
            print(_sum)
            continue
        _sum += (c-b)*_val
        print(_sum)
        count_list[b-1] = 0
        count_list[c-1] += _val

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    num = int(input())
    trials = [map(int, input().split()) for _ in range(num)]
    run(n, seq, num, trials)