from operations import *

# ops = {(1,mod_sum), (2,mod_subtr), (3, )}

def calculate(operation, a, b, mod):
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



def input_operand(message):
    try:
        return int(input(message))
    except ValueError as ex:
        print("Operand must be integer")
        return input_operand(message)


def input_operation(message):
    try:
        operation = int(input(message))
    except ValueError as ex:
        print("Operation must ba integer")
        operation = input_operation(message)
    if operation not in range(1, 11):
        print("Invalid operation")
        return input_operation(message)
    return operation


print("It's a modulo calculator, all operations are already mod")
a = input_operand("Input first operand: \n ")
mod = input_operand("Input mod: \n ")
operation = input_operation(
    """Input operation number:
    1 -> +
    2 -> -
    3 -> *
    4 -> /
    5 -> pow
    6 -> compare
    7 -> is quadratic residue?
    8 -> %
    9 -> inverse a
    10 -> square root
    """)

b = input_operand("Input second operand: \n") if operation < 7 else None
print("result: " , calculate(operation, a, b, mod))

