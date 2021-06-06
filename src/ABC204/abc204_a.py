if __name__ == '__main__':
    x,y = map(int, input().split())
    if x != y:
        ans = [i for i in [0, 1, 2] if i not in [x, y]]
        print(ans[0])
    else:
        print(x)