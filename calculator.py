from operations import *

# ops = {(1,mod_sum), (2,mod_subtr), (3, )}

def calculate(operation):
    if operation == 1:
        return mod_sum(a, b, mod)
    if operation == 2:
        return mod_subtr(a, b, mod)
    if operation == 3:
        return mod_mult(a, b, mod)
    if operation == 4:
        return mod_div(a, b, mod)
    if operation == 5:
        return mod_pow(a,b, mod)
    if operation == 6:
        return  mod_compare(a, b, mod)
    if operation == 7:
        return is_quadratic_residue(a, mod)
    if operation == 8:
        return module(a, mod)
    if operation == 9:
        return mod_inverse(a, mod)
    if operation == 10:
        return modular_sqrt(a, mod)

print("It\'s a modulo calculator, all operations are already mod")
a = input("Input first operand \n ")
mod = input("Input mod \n ")
operation = input("Input operation number: \n"
"1 -> + \n 2 -> - \n 3 -> * \n 4 -> / \n 5 -> pow \n 6 -> compare \n"
"7 -> is quadratic residue? \n 8 -> |a|  \n 9 -> inverse a \n 10 -> square root \n")
if operation < 7:
    b = input("Input second operand  \n")

print "result: " , calculate(operation)

