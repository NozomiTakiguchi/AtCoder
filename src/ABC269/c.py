# https://qiita.com/masayoshi64/items/0be4bce77783b6013b34
# bitDP で解ける、みたいなツイート見た。 bitDP と bit全探索の違いって何？？
def run(x):
    _x = bin(x)[2:]
    ans = '0'.zfill(len(str(_x)))
    l = [True if int(e) else False for e in _x]
    cnt = 2**sum(l)

    for i in range(x):
        _ans = i+1
        





if __name__ == '__main__':
    x = int(input())
    run(x)