def extended_euclid(a, b):
    if b == 0:
        return [a, 1, 0]
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while b > 0:
        q = a // b
        a, b = b, a - q * b
        x1, x2 = x2 - q * x1, x1
        y1, y2 = y2 - q * y1, y1
    return [a, x2, y2]