'''
abbaac -> [[a,1][b,2][a,2][c,1]]
'''
def run_length_encoding(s: str) -> list(list()):
    prev = ''
    rle = [[prev, 1]]
    for e in s:
        if prev == e:
            rle[-1][1] += 1
        elif prev == '':
            rle[-1][0] = e
        else:
            rle.append([e, 1])
        prev = e

    return rle

def run(s,t):
    rle_s, rle_t = run_length_encoding(s), run_length_encoding(t)

    if len(rle_t) != len(rle_s):
        print('No')
        exit()

    for i,e in enumerate(rle_t):
        s_char, s_cnt = rle_s[i]
        t_char, t_cnt = e

        if t_char != s_char:
            print('No')
            exit()
        
        if t_cnt != s_cnt:
            if t_cnt < s_cnt:
                print('No')
                exit()
            elif s_cnt < 2:
                print('No')
                exit()
    print('Yes')


if __name__ == '__main__':
    s = input()
    t = input()
    run(s,t)