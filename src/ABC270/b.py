x,y,z = map(int, input().split())

#ゴールとの間に壁があるかどうか
wall = False
if 0 < x:
    if 0 < y and y < x:
        wall = True
    
    # x も y も正
    if wall:
        if y < z:
            print(-1)
            exit()
        else:
            if z < 0:
                print(abs(2*z) + x)
                exit()
            else:
               print(x)
               exit()
    else:
        print(x)
        exit()
else:
    if y < 0 and x < y:
        wall = True
    # x も y も負
    if wall:
        if z < y:
            print(-1)
            exit()
        else:
            if z > 0:
                print(abs(2*z) + abs(x))
                exit()
            else:
                print(abs(x))
                exit()
    else:
        print(abs(x))
        exit()

