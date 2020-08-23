def run():
    '''
    複数行 2 数値
    https://qiita.com/zenrshon/items/c4f3849552348b3dbe67
    '''
    xy = [map(int, input().split()) for _ in range(5)]
    print(xy)

    x, y = [list(i) for i in zip(*xy)]
    print('x={}, y={}'.format(x, y))


if __name__ == "__main__":
    run()