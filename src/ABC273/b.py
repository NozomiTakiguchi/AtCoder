from decimal import Decimal,ROUND_HALF_UP
x,k = map(int, input().split())

for i in range(k):
    tgt = '1E'+str(i+1)
    x = int(Decimal(x).quantize(Decimal(tgt), rounding=ROUND_HALF_UP))

print(x)