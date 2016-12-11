from helpers import *


def mod_sum(a, b, mod):
    return (abs(a + b)) % mod


def mod_subtr(a, b, mod):
    return (abs(a - b)) % mod


def mod_mult(a, b, mod):
    return (abs(a * b)) % mod


def mod_div(a, b, mod):
    return abs(a // b) % mod


def mod_pow(a, b, mod):
    return pow(a, b, mod)


def module(a, mod):
    return (a % mod)


def mod_compare(a, b, mod):
    if (a % mod) > (b % mod):
        return ">"
    elif (a % mod) == (b % mod):
        return "="
    return "<"


def is_quadratic_residue(a, mod):
    if legendre_symbol(a, mod) == -1:
        return False
    if legendre_symbol(a, mod) == 0:
        return 0
    else:
        return True


def mod_inverse(a, mod):
    trinity = extended_euclid(a, mod)
    if trinity[0] > 1:
        return "doesn't exist"
    return trinity[1] if trinity[1] >= 0 else mod + trinity[1]


def modular_sqrt(a, p):  # 10 mod 53 = 13
    res = []
    for i in Factor(p):
        x = prime_mod_sqrt(a, i)
        res.append(x)
        res.append(i - x)
    return {x for x in res if pow(x, 2, p) == a % p}
