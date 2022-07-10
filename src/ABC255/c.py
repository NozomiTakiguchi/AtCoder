
'''
二分探索で解ける
初項 a 公差 d 工数 n の等差数列
6 2 3 3 → S = (2, 5, 8)
'''

def run(x,a,d,n):
    left = 0
    right = n-1

    sleft = a
    sright = sleft + (d*right)
    ans = min(abs(x-sright), abs(sleft-x)) # 数列の外の場合を考慮


    while right - left > 1:
        mid = left + (right-left)//2
        t = a+d*mid

        if x >= t:
            ans = min(abs(x-t), ans)
            if a < t:
                left = mid
            else: # 単調減少の場合
                right = mid
        elif x <= t:
            ans = min(abs(t-x), ans)
            if a < t:
                right = mid
            else: # 単調減少の場合
                left = mid
    
    print(ans)


if __name__ == '__main__':
    x, a, d, n = list(map(int, input().split()))
    run(x,a,d,n)