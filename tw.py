import matplotlib.pyplot as plt

# Created empty list to keep track of values for ploting
x_values = []
y_values = []


def f(x, y):
    return eval(equation)  # Evaluate the user-provided equation


def rk4(x0, y0, xn, h):
    """
    Runge-Kutta Fourth Order method implementation.

    Args:
        x0 (float): Initial value of x.
        y0 (float): Initial value of y.
        xn (float): Calculation point where y is evaluated.
        h (float): Step size.
    """
    print("\n----------- Iteration Table -----------")
    print("n\t x(n)\t\ty(n)\t\ty(n+1)")
    print("---------------------------------------")

    # n (int): Number of steps(Iteration).
    n = (int)((xn - x0) / h)

    x_values.append(x0)
    y_values.append(y0)

    i = 0
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)

        # Assuming k1, k2, k3, and k4 are already defined variables with their respective values

        # Round the values to 4 decimal places
        k1_rounded = round(k1, 4)
        k2_rounded = round(k2, 4)
        k3_rounded = round(k3, 4)
        k4_rounded = round(k4, 4)

        # Print the rounded values
        print("k1: ", k1_rounded, "k2: ", k2_rounded, "k3: ", k3_rounded, "k4: ", k4_rounded)

        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6

        k_rounded = round(k, 4)
        print("k: ", k_rounded)

        yn = y0 + k

        y_values.append(yn)

        print(i + 1, "\t", f"\t{yn:.4f}")
        i += 1

        y0 = yn
        x0 += h

        x_values.append(x0)

    print("\nAt x = {:.6f}, y = {:.6f}".format(xn, yn))


print(">>>>>>>>>>>> RK Method of Order 4 <<<<<<<<<<<<")

# main()
# User inputs
equation = input("Enter the f(x,y): ")
x0 = float(input("Enter initial value of x (x0): "))
y0 = float(input("Enter initial value of y (y0): "))
xn = float(input("Enter calculation point (xn): "))
step_size = float(input("Enter step size (h): "))

# Call RK4 method
rk4(x0, y0, xn, step_size)

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('RK Method of Order 4')
plt.grid(True)
plt.show()

# f(x, y): -(2*y)/x + 2/(3*x) - (4*(1)*(x))/3
#  initial value of x: 0.1
# initial value of y: 0.1
# step size (h): 0.7
# calculation point (xn): 5

# function f(x, y): -(x * y**2 + y)
# initial value of x: 0
# initial value of y: 1
# step size (h): 0.1
# calculation point (xn): 1
