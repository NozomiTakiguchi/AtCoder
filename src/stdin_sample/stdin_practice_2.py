import sys
def run():
    '''
    連続文字 int
    ex. in : 12 34 56 / out; [12,34,56]
    https://qiita.com/zenrshon/items/c4f3849552348b3dbe67
    '''
    _in = list(map(int, input().split()))

    print(_in)


if __name__ == '__main__':
    run()