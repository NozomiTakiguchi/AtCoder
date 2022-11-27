import math

def main(a,b):
    i = 1
    l = []
    while a > 1:
        a = a/math.sqrt(i)
        i+=1
        l.append(a)
    
    ans = []
    for i,e in enumerate(l):
        ans.append(b*(i+1)+e)
    
    print(ans)







if __name__ == '__main__':
    a,b = map(int, input().split())
    main(a,b)