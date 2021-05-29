n = int(input())
num_list = list(map(int, input().split()))

_sum =0 
_list = []
length = 1
for e in num_list:
    _list.append(e)
    _m = e
    _sum += sum(_list)
    ans = _m*length + _sum

    print(ans)
    length += 1