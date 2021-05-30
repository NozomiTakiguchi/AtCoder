import collections


if __name__ == '__main__':
    _l = list(map(int, input().split()))

    if len(list(set(_l))) == 3:
        print(0)
        exit()
    elif len(list(set(_l))) == 1:
        print(_l[0])
        exit()
    
    c = collections.Counter(_l)
    print(c.most_common()[-1][0])


