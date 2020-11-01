from collections import Counter
def run(n):
    '''
    '''
    # ↓ は模範解答. 時間がなくて解けなかった

    if len(n) <= 2:
        # 2 桁の場合は、それぞれの数字を入れ替えたものも考慮する    
        if n%8 == 0 or int(n[::-1]) %8 == 0:
            print('Yes')
        else:
            print('No')
        return


    cnt = Counter(n)
    
    # 3 桁の 8 の倍数を回していく
    for i in range(112, 1000, 8):
        # 文字列は iterable
        if not Counter(str(i)) - cnt:
            print("Yes")
            exit()
    print('No')
        



if __name__ == '__main__':
    n = input()
    run(n)