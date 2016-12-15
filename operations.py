from helpers import *


def mod_sum(a, b, mod):
    return (abs(a + b)) % mod


def mod_subtr(a, b, mod):
    return (abs(a - b)) % mod


def mod_mult(a, b, mod):
    return (abs(a * b)) % mod


def mod_div(a, b, mod):
    inverse = mod_inverse(b, mod)
    if inverse.isnumeric():
        return mod_mult(a, inverse, mod)
    return 'Cannot divide'


def mod_pow(a, b, mod):
    return pow(a, b, mod)


def module(a, mod):
    return a % mod


def is_comparable(a, b, mod):
    return (a % mod) == (b % mod)


def is_quadratic_residue(a, mod):
    return len(modular_sqrt(a, mod)) > 0


def mod_inverse(a, mod):
    trinity = extended_euclid(a, mod)
    if trinity[0] > 1:
        return "doesn't exist"
    return trinity[1] % mod


def modular_sqrt(a, p):
    return [i for i in range(p) if mod_pow(i, 2, p) == a % p]
