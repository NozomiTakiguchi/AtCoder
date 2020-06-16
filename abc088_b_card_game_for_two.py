def run():
    '''
    N 枚のカードがあり、i 枚目のカードには ai という数が書かれています。
    Alice と Bob はこれらのカードを使ってゲームを行います。
    ゲームでは 2 人が交互に 1 枚ずつカードを取っていきます。Alice が先にカードを取ります。
    2 人がすべてのカードを取ったときゲームは終了し、
    取ったカードの数の合計がその人の得点になります。
    2 人とも自分の得点を最大化するように最適戦略をとったとき、Alice は Bob より何点多くの得点を獲得できるかを求めてください。

    [制約]
    N は 1 以上 100 以下の整数
    ai は 1 以上 100 以下の整数
    [数値例]
    N = 3
    a = (2,7,4)
    答え : 5
    '''
    _in_n = int(input()) # not use...
    _cards = list(map(int, input().split()))

    # index of enumerate starts from 0
    # both list.sort() and sorted(list) by default sort elements in ascending order
    score_of_alice = sum([n for i,n in enumerate(sorted(_cards, reverse=True)) if (i+1)%2 != 0])
    score_of_bob = sum([n for i,n in enumerate(sorted(_cards, reverse=True)) if (i+1)%2 == 0])
    print('alice will get [{}]. bob will get [{}]. diff = [{}]'.format(score_of_alice, score_of_bob, score_of_alice - score_of_bob))




if __name__ == '__main__':
    run()