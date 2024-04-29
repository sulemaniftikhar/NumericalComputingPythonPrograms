# import numpy
#
# # Given values for M, q, and r
# M = 1
# q = 1
# r = 1
#
# # Define the left-hand side of the equations
# left_side = numpy.array([[1 - (2 * M / r) + (3 * M * q ** 2 / r ** 3), 0, 0],
#                          [0, 1 - (2 * M / r) + (3 * M * q ** 2 / r ** 3), 0],
#                          [0, 0, 1 - (2 * M / r) + (3 * M * q ** 2 / r ** 3)]])
#
# # Define the right-hand side of the equations
# right_side = numpy.array([0, 0, 0])
#
# # Solve for x, y, and z
# solution = numpy.linalg.solve(left_side, right_side)
# # Extract the values
# x, y, z = solution
#
# print(f"Value of x: {x:.4f}")
# print(f"Value of y: {y:.4f}")
# print(f"Value of z: {z:.4f}")

import sympy


def equations():
    M, r, q = sympy.symbols('M r q', real=True, positive=True)
    x, y, z = sympy.symbols('x y z', real=True)

    eq1 = 1 / r + 2 * M * q ** 2 / r ** 3 - x ** 2 * r ** 2
    eq2 = (1 / r + 2 * M * q ** 2 / r ** 3) * (y ** 2 / (x + z * r) ** 2)
    eq3 = sympy.diff((1 / r + 2 * M * q ** 2 / r ** 3) * (y ** 2 / (x + z * r) ** 2), r)

    return eq1, eq2, eq3


eq1, eq2, eq3 = equations()

# Define x, y, z
x, y, z = sympy.symbols('x y z', real=True)

sol = sympy.solve([eq1, eq2, eq3], [x, y, z])

for solution in sol:
    print(sympy.simplify(solution))
