# 全く納得感はないけど一応 AC
# S のうち、 1 が Si ~ Si+k-1 の中に全部含まれる & 同じ範囲に 0 が含まれない、が必要十分条件
# → 与えられた S にあらかじめ含まれている 1 が全部範囲内にある時だけ、というのが、実際そうなんだけど納得感がない
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k = map(int, input().split())
        s = input()
        m = s.count("1") # 文字列全体で 1 がいくつ含まれているか

        cnt0 = s[:k].count("0") # 最初の k 文字における 0 の個数
        cnt1 = s[:k].count("1") # 最初の k 文字における 1 の個数
        cnt = 0

        for i in range(n-k):
            if cnt1 == m and cnt0 == 0: # Si ~ Si+k-1 が 1 と ? からなる場合
                cnt += 1
            if s[i] == "1":
                cnt1 -= 1
            elif s[i] == '0':
                cnt0 -= 1
            
            if s[i+k] == '1':
                cnt1 += 1
            elif s[i+k] == '0':
                cnt0 += 1
        
        if cnt1 == m and cnt0 == 0:
            cnt += 1
        
        if cnt == 1:
            print('Yes')
        else:
            print('No')
