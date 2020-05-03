import decimal

print(decimal.Decimal(1.0)/decimal.Decimal('3.0'))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.0')/decimal.Decimal('3.0'))
print(decimal.Decimal('1.0')/decimal.Decimal('3.0'))