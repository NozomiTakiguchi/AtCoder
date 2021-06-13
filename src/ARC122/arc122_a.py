# DP を解けば求まるらしいので DP キャッチアップする
def run(n):
    a = list(map(int, input().split()))

    # print(1+sum([i+1 for i in range(n-2)]))
    rep = 1+sum([i+1 for i in range(n-2)])
    # if len(a) == 1:
    #     print(sum(a))
    #     exit()
    # elif len(a) == 2:
    #     ans = 2*sum(a) - 2*a[1]
    #     print(ans)
    #     exit()
    # elif len(a) == 3:
    #     ans = 3*sum(a) - 2*a[1] - 2*a[2]
    #     print(ans)
    #     exit()
    print((rep+1)*sum(a) - 2*(n-2)*a[1] - 2*(n-2)*a[-1])
    
    ans = sum(a)





if __name__ == '__main__':
    n = int(input())
    run(n)