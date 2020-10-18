def run(x, y, a, b):
    '''
    A. カコモンジム -> ✖a
    B. AtCoder ジム -> ️+b

    → A に何回か通った後に B ジムに通った方がいい
    → B -> A の順 (2 回のトレーニング) だと強さが Z -> Z + b -> aZ + ab  となるが、これは　A -> B -> B -> ... -> B (A に通った後 B に a 回通うのと同じだから. すなわち 1+ a 回のトレーニング)
    '''

    experience_point = 0

    # a 倍した値が a+b より大きくなると、すくなくとも訓練を 1 回は損してしまう
    while a*x <= a+b and a*x < y:
        x*=a
        experience_point += 1
    # y 以上にならないように訓練するので、 y-1 しておく
    experience_point = experience_point + (y-1-x)//b
    print(experience_point)

if __name__ == '__main__':
    # いっつもリスト作って分割代入させてたけど、しなくても問題ない
    x, y, a, b= map(int, input().split())
    run(x, y, a, b)