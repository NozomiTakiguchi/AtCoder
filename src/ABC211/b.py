_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    s = []
    s1 = _i()
    s2 = _i()
    s3 = _i()
    s4 = _i()
    s.append(s1)
    s.append(s2)
    s.append(s3)
    s.append(s4)

    if len(set(s)) == len(set(['H','2B','3B','HR'])):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    run()
