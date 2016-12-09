def extended_euclid(a, b):
    if b == 0:
        return [a, 1, 0]
    # x2, y2 -- Bézout coefficients
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    while b > 0:
        q = a // b
        a, b = b, a - q * b
        x1, x2 = x2 - q * x1, x1
        y1, y2 = y2 - q * y1, y1
    return [a, x2, y2]


def legendre_symbol(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls
