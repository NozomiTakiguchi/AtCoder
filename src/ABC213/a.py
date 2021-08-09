_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    a,b = _l()
    # for i in range(256):
    #     if a^(i) == b:
    #         print(i)
    #         exit()
    
    # a xor a = 0 が成り立つため、 a xor c = b の両辺に a を xor すれば、 c = b xor a
    print(a^b)

if __name__ == '__main__':
    run()
