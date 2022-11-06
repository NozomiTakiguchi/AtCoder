from decimal import Decimal,ROUND_HALF_UP

a,b = map(int, input().split())
print(str(Decimal(str(b/a)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).ljust(4,'0'))
