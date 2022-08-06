if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))

    ans = 1
    _p = p[-1]
    while _p !=1:
        _p = p[_p-2]
        ans += 1
    
    print(ans)