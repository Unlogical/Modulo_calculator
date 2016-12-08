from operations import *


unary_operations = {
    "?" : is_quadratic_residue,
    "%" : module,
    "~" : mod_inverse,
    "sqrt" : modular_sqrt
}

binary_operations = {
    "+" : mod_sum,
    "-" : mod_subtr,
    "*" : mod_mult,
    "/" : mod_div,
    "^" : mod_pow,
    "=" : mod_compare
}


def calculate(operation, mod, a, b):
    if operation in binary_operations:
        return binary_operations[operation](a, b, mod)
    return unary_operations[operation](a, mod)


def input_operand(message):
    try:
        return int(input(message))
    except ValueError as ex:
        print("Operand must be integer")
        return input_operand(message)


def input_operation(message):
    operation = input(message).strip()
    if operation in binary_operations or operation in unary_operations:
        return operation
    else:
        print("Invalid operation")
        return input_operation(message)


print("It's a modulo calculator, all operations are already mod")
a = input_operand("Input first operand: \n ")
mod = input_operand("Input mod: \n ")
operation = input_operation(
    """Input operation:
    + -> sum
    - -> substraction
    * -> multiplication
    / -> division
    ^ -> power
    = -> compare
    ? -> is quadratic residue?
    % -> mod
    ~ -> inverse a
    sqrt -> square root
    """)

b = input_operand("Input second operand: \n") if operation in binary_operations else None
print("result: ", calculate(operation, mod, a, b))

