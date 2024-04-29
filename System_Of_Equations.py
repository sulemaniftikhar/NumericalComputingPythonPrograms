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

# Answer
# (-sqrt(2*M*q**2 + r**2)/r**(5/2), 0, z)
# (sqrt(2*M*q**2 + r**2)/r**(5/2), 0, z)
