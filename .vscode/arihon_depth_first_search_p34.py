def run(n, _in_list, k):
    '''
    部分和問題. 深さ優先探索はその性質上、再帰処理で簡単に書くことができるらしい. TODO アルゴリズム理解.
    '''

    # depth-first search
    def dfs(i, sum):

        if i == n:
            return sum == k
        if dfs(i+1, sum):
            return True
        if dfs(i+1, sum + _in_list[i]):
            return True
        return False
    
    print('yes' if dfs(0, 0) else 'no')



if __name__ == '__main__':
    n = int(input())
    _in_list = list(map(int, input().split()))
    k = int(input())
    run(n, _in_list, k)