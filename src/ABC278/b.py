h,m = input().split()

while True:
    h = h.zfill(2)
    m = m.zfill(2)
    if int(h[0]+ m[0]) <= 23 and int(h[1]+m[1]) <= 59:
        print(h,m)
        exit()
    else:
        m = str((int(m)+1)%60)
        h = str((int(h)+1)%24) if int(m) == 0 else h
