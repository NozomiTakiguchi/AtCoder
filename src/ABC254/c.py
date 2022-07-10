'''
解説読んでも訳が分からない。
スワップ系の問題は剰余使ったらうまくいきそう、ってことだけ暗記してしまったほうがよさそう
'''

def run(n,k,a):
    b = [[] for i in range(k)] # 剰余が一致するところはスワップできる

    # スワップできる要素をそれぞれのリストに加える
    for i in range(n):
        idx = i%k # 余りは 0 <= idx <= k-1 のいずれか = b の要素数と一致
        b[idx].append(a[i])

    l_sorted = []
    # わざわざ自作でマージソートする必要ない
    # スワップできる要素でまとめられた各リストをソートする
    for e in b:
         l_sorted.append(sorted(e))
    

    l = []
    # 元に戻す (厳密には、スワップできる要素がもともといた位置に、要素をソートしたうえではめ込む)
    for i in range(n):
        q,mod = divmod(i,k) # 商と余り
        l.append(l_sorted[mod][q])

    asc = True
    # 昇順になっていれば OK
    for i in range(len(l)-1):
        if l[i] <= l[i+1]:
            continue
        else:
            asc = False
            break
    
    print('Yes') if asc else print('No')
    exit()


if __name__ == '__main__':
    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    run(n,k,a)
