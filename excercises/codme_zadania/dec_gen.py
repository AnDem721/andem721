from decimal import Decimal
def gen_dec():
    return [Decimal(x) /Decimal(2) for x in range(4,12)]
print(gen_dec())

