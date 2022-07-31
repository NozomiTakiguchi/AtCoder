def run(n, a):
    cnt = 0
    ans = 0
    for i,e in enumerate(a):
        if i+1 == e:
            cnt += 1
            continue
        if a[e-1] == i+1:
            ans += 1
    ans /= 2 # 重複排除
    ans += (cnt*(cnt-1))/2
    print(int(ans))




if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    run(n,a)