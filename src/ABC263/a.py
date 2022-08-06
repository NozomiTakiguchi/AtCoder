if __name__ == '__main__':
    l = sorted(list(map(int, input().split())))

    if len(list(set(l))) != 2:
        print('No')
        exit()
    
    p1,p2 = l[0],l[-1]
    p1_cnt = 0
    p2_cnt = 0
    for e in l:
        if e == p1:
            p1_cnt += 1
        else:
            p2_cnt += 1
    
    if p1_cnt == 3 and p2_cnt == 2:
        print('Yes')
    elif p1_cnt == 2 and p2_cnt == 3:
        print('Yes')
    else:
        print('No')