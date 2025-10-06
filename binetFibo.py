import decimal

def binetFibo(n) :
    r5 = decimal.Decimal('5').sqrt()
    phi = (1+r5) / 2
    psi = (1-r5) / 2
    return round((pow(phi, n) - pow(psi, n)) / r5)
    
print(binetFibo(10000))
