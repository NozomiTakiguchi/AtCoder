from decorator import trace_perf

@trace_perf
def run(x, n, num_array):
    '''
    整数 X と、長さ N の整数列 p1 , … , pN が与えられます。
    整数列 p1 , … , pN に含まれない整数 (正とは限らない) のうち X に最も近いもの、つまり X との差の絶対値が最小のものを求めてください。
    そのような整数が複数存在する場合は、そのうち最も小さいものを答えてください。

    [入力例]
    6 5
    4 7 10 6 5
    [出力例]
    8  //整数列 4, 7, 10, 6, 5 に含まれない整数のうち、最も 6 に近いものは 8 
    '''
    if len(num_array) == 0:
        print(x)
        return
    
    i = 0
    while True:
        if x - i not in num_array:
            print(x - i)
            return
        elif x + i not in num_array:
            print(x + i)
            return
        i += 1
        

if __name__ == '__main__':
    x, n = list(map(int, input().split()))
    num_array = list(map(int, input().split()))
    run(x, n, num_array)