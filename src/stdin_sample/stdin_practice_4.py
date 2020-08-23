def run():
    '''
    複数行数値. ここから正方形の行列を作成
    https://qiita.com/zenrshon/items/c4f3849552348b3dbe67
    '''
    _in = [[int(c) for c in input().strip()] for _ in range(3)]

    print(_in)



if __name__ == "__main__":
    run()