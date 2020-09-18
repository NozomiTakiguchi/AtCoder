def run(max_num, _in_list, target_value):
    '''
    [問題] 
    整数が n 個与えられます。その中からいくつか選び、その和をちょうど k にすることができるかを判定してください。
    =====
    → 部分和問題. 深さ優先探索はその性質上、再帰処理で簡単に書くことができるらしい. TODO アルゴリズム理解.
    '''

    # depth-first search
    # 途中で目的の値が取得できた時、 true が連鎖的に帰ってきて最終的に本体の関数が true になるような構造
    def dfs(i, current_sum):
        if i == max_num: 
            print('1st if-statement. i = {}. sum = {}'.format(i, current_sum))
            return current_sum == target_value # 渡されたインプットを全て使い、目的の値を構成することができるか否かを判断
        if dfs(i+1, current_sum):
            print('2nd if-statement. i = {}. sum = {}'.format(i, current_sum))
            return True
        if dfs(i+1, current_sum + _in_list[i]):
            print('3rd if-statement. i = {}. sum = {}'.format(i, current_sum))
            return True
        return False
    
    print('yes' if dfs(0, 0) else 'no')



if __name__ == '__main__':
    n = int(input())
    _in_list = list(map(int, input().split()))
    k = int(input())
    run(n, _in_list, k)