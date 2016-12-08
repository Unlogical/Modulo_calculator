from helpers import *

def mod_sum(a, b, mod):
    return (abs(a + b)) % mod

def mod_subtr(a, b, mod):
    return(abs(a - b)) % mod

def mod_mult(a, b, mod):
    return (abs(a*b)) % mod

def mod_div(a, b, mod):
    return (abs(a // b) % mod)

def mod_pow(a, b, mod):
    return pow(a, b, mod)

def module(a, mod):
    return(a % mod)

def mod_compare(a, b, mod):
    if (a % mod) > (b % mod):
        return ">"
    elif (a % mod) == (b % mod):
        return  "="
    return  "<"


def is_quadratic_residue(a, mod):
    if legendre_symbol(a, mod) == -1:
        return False
    if legendre_symbol(a, mod) == 0:
        return 0
    else:
        return True


def mod_inverse(a, mod):
    trinity = extended_evklid(a, mod)
    if trinity[0] > 1:
        return "doesn't exist"
    return trinity[1] if trinity[1] >= 0 else mod + trinity[1]


def modular_sqrt(a, p): #10 mod 53 = 13

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m




















