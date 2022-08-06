'''長さ N かつ全ての要素が 1 以上 M 以下である整数列のうち、狭義単調増加であるものを全て辞書順に出力してください。
'''

# 超簡単なのになぜか悩んでしまった。。。。。。
# マジで A~C まで 20 分くらいで出来るはずだったのに タイムアップ
# import itertools
# def run(n,m):
#     l = list(itertools.combinations(range(1,m+1), n))
#     for e in l:
#         print(*e)

'''
解説では dfs 使っててさらに意味わからない
'''
# 深さ優先では、一番深いところの loop から消費していく
def dfs(l,n,m):
    print(l)
    if len(l) == n:
        print(*l)
        return
    if len(l) == 0:
        start = 1
    else:
        start = l[-1]+1
    for i in range(start, m+1):
        dfs(l+[i], n, m)




if __name__ == '__main__':
    n,m = map(int, input().split())
    # run(n,m)
    dfs([], n, m)