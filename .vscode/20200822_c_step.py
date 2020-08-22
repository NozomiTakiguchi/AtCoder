def run(x, a_list):
    '''
    see. https://atcoder.jp/contests/abc176/tasks/abc176_c
    '''
    if x == 1:
        print(0)
    else:
        out = 0
        prev = 0
        for i,v in enumerate(a_list):
            if i == 0:
                continue
            prev_height = prev + a_list[i-1]
            if v > prev_height:
                out += 0
                prev = 0
            else:
                out += prev_height - v
                prev = prev_height - v
            
        print(out)
            


    



if __name__ == '__main__':
    x = int(input())
    a_list = list(map(int, input().split()))
    run(x, a_list)