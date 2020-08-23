
def run(a, b, c, s):
    '''
    高橋君はデータの加工が行いたいです。
    整数 a, b, c と、文字列 s が与えられます。 
    a + b + c
    の計算結果と、文字列 
    s
    を並べて表示しなさい。
    '''
    print('{} {}'.format(a + b + c, s))

if __name__ == '__main__':
    a = int(input())
    b, c = list(map(int, input().split()))
    s = input()
    run(a, b, c, s)