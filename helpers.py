def extended_evklid(a, b):
    if b == 0:
        return [a, 1, 0]
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while b > 0 :
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return [a, x2, y2]


def legendre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls
