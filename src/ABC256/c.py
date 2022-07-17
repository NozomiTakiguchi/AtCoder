'''
各要素の和を求めるような問題は、最後の要素はそれまでの要素の合計で一位に定まるので時限を一つ下げることができる
'''
def run(n):
    if sum(n[:3]) != sum(n[3:]):
        print(0)
        exit()
    
    h1, h2, h3, w1, w2, w3 = n

    ans = 0
    for a in range(1,29):
        for b in range(1,29):
            for d in range(1,29):
                for e in range(1,29):
                    c = h1 - a - b
                    f = h2 - d - e
                    g = w1 - d - a
                    h = w2 - e - b
                    i = w3 - f - c
                    if min([c,f,g,h,i]) > 0 and i == h3 - g - h:
                        ans+=1

    print(ans)

# '''
# dfs でも解けるらしいのでやってみる
# [[0,0,0],[0,0,0],[0,0,0]] で初期化
# n => インデックスとする
# '''
# a = [[0]*3 for _ in range(2)]
# ans = 0
# def dfs(ij, l):
#     print()

#     i = int(ij/3)
#     j = int(ij%3)
#     # return の条件
#     if i == 3:
#         global ans
#         ans += 1
#         return
#     if i == 2:
#         x = l[2+j] - a[0][j] - a[1][j]
#         if x <= 0:
#             return
#         a[i][j] = x
#         dfs(ij+1, l)
#     elif j == 2:
#         x = l[i] - a[i][0] - a[i][1]
#         if x <= 0:
#             return 
#         a[i][j] = x
#         dfs(ij+1, l)
#     else:
#         for x in range(1,29):
#             a[i][j] = x
#             dfs(ij+1, l)


if __name__ == '__main__':
    n = list(map(int, input().split()))
    run(n)
    # dfs(0, n)
    # print(ans)