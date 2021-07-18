from collections import defaultdict
_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n,k = _l()
    c = _l()

    dic = defaultdict(int)
    starts = c[:k]
    for e in starts:
        dic[e] += 1
    
    ans = []
    ans.append(len(dic))
    for i,e in enumerate(c[k:]):
        _e = c[i]
        dic[_e] -= 1
        dic[e] += 1

        if dic[_e] == 0:
            del dic[_e]
        
        ans.append(len(dic))

    
    print(max(ans))




if __name__ =='__main__':
    run()