import sympy
import matplotlib.pyplot as plt

x_values = []
y_values = []


def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method for finding the root of a function.

    Args:
        f (function): The function for which we want to find the root.
        df (function): The derivative of the function.
        x0 (float): Initial guess for the root.
        tol (float, optional): Tolerance for convergence. Defaults to 1e-6.
        max_iter (int, optional): Maximum number of iterations. Defaults to 100.

    Returns:
        float: The approximate root of the function.
    """

    x_values.append(x0)

    x = x0
    print("\n----------- Iteration Table -----------")
    print("n\t\t x(n)\t\t\tx(n+1)")
    print("---------------------------------------")
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        y_values.append(x_new)

        print(i, "\t\t", f"{x:.6f}\t\t{x_new:.6f}")

        if abs(x_new - x) < tol:
            return x_new
        x = x_new
        x_values.append(x)
    raise ValueError("Newton-Raphson method did not converge.")


print(">>>>>>>>>>>> Newton Raphson Method <<<<<<<<<<<<")

# main()
# Example usage: user input for equation and initial guess
equation = input("Enter your equation (in terms of x): ")
initial_guess = float(input("Enter an initial guess for the root: "))

# Define the function and its derivative based on user input
x = sympy.symbols('x')
expr = sympy.sympify(equation)
f = sympy.lambdify(x, expr)

# Calculate the derivative symbolically
df = sympy.lambdify(x, sympy.diff(expr, x))

# Find the root using Newton-Raphson method
root = newton_raphson(f, df, initial_guess)
print(f"Approximate root: {root:.6f}")

# Plotting
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('x(n+1)')
plt.title('Newton Raphson Method')
plt.grid(True)
plt.show()

# Q1 2*x**3 - 2*x - 5 , initial guess = 0
# Q2 2**x - x - 1.7 , initial guess = 0