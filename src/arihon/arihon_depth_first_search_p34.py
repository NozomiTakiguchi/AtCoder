def run(n, _in_list, k):
    '''
    部分和問題. 深さ優先探索はその性質上、再帰処理で簡単に書くことができるらしい. TODO アルゴリズム理解.
    '''

    # depth-first search
    # 途中で目的の値が取得できた時、 true が連鎖的に帰ってきて最終的に本体の関数が true になるような構造
    def dfs(i, sum):
        print('i={}'.format(i))
        if i == n:
            print('i={}, sum={}, first if-statement'.format(i, sum))
            return sum == k
        if dfs(i+1, sum):
            print('i={}, sum={}, second if-statement'.format(i, sum))
            return True
        if dfs(i+1, sum + _in_list[i]):
            print('i={}, sum={}, third if-statement'.format(i, sum))
            return True
        return False
    
    print('yes' if dfs(0, 0) else 'no')



if __name__ == '__main__':
    n = int(input())
    _in_list = list(map(int, input().split()))
    k = int(input())
    run(n, _in_list, k)