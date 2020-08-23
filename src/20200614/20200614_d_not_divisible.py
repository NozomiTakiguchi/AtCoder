from decorator import trace_perf
import copy

@trace_perf
def run(n, num_array):
    '''
    長さ N の数列 A が与えられます。 次の性質を満たす整数 i (1 ≤ i ≤ N) の数を答えてください。 
        i ≠ j である任意の整数 j (1 ≤ j ≤ N) について A i は A j で割り切れない
    [制約]
    入力はすべて整数
    1 ≤ N ≤ 2×10^5
    1 ≤ Ai ≤ 10^6

    [入力例]
    5
    24 11 8 3 16
    [出力例]
    3 // 問の性質を満たすのは 2, 3, 4 (リストの他の任意の要素で割り切れないものを数える)
    '''

    # 約数を求める. √n まで調べれば約数の全量を取得することができる
    def divisor(n):
        i = 1
        table = []
        while i * i <= n:
            if n%i == 0: # i が n の約数である場合、 n/i も n の約数
                table.append(i)
                table.append(n//i)
            i += 1
        return set(table)
    
    # FIXME 実行スピードが遅すぎて TLE になりまくった. 
    count = 0
    for i in range(len(num_array)):
        _list = copy.deepcopy(num_array)
        del _list[i]
        if len(divisor(num_array[i]) & set(_list)) >= 1:
            continue
        count += 1

    print(count)

if __name__ == "__main__":
    n = int(input())
    num_array = list(map(int, input().split()))
    run(n, num_array)