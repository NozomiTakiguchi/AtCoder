def run(a, b, c):
    if c%2 == 0:
        if abs(a) == abs(b):
            print('=')
        else:
            print('<' if abs(a) < abs(b) else '>')
    else:
        if a == b:
            print('=')
        else:
            print('<' if a < b else '>')


if __name__ == '__main__':
    a,b,c = map(int, input().split())
    run(a, b, c)