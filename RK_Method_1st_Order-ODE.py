import matplotlib.pyplot as plt

# Created empty lists to keep track of values for plotting
x_values = []
y_values = []
z_values = []


def f(x, y, z):
    return eval(equation_f)  # Evaluate the user-provided equation for f(x, y, z)


def g(x, y, z):
    return eval(equation_g)  # Evaluate the user-provided equation for g(x, y, z)


def rk4(x0, y0, z0, xn, h):
    """
    Runge-Kutta Fourth Order method implementation.

    Args:
        x0 (float): Initial value of x.
        y0 (float): Initial value of y.
        z0 (float): Initial value of z.
        xn (float): Calculation point where y is evaluated.
        h (float): Step size.
    """
    print("\n----------- Iteration Table -----------")
    print("n\t x(n)\t\ty(n)\t\tz(n)\t\ty(n+1)\t\tz(n+1)")
    print("---------------------------------------")

    # n (int): Number of steps (Iterations).
    n = int((xn - x0) / h)

    x_values.append(x0)
    y_values.append(y0)
    z_values.append(z0)

    while x0 < xn:
        k1 = h * f(x0, y0, z0)
        l1 = h * g(x0, y0, z0)

        k2 = h * f(x0 + h / 2, y0 + k1 / 2, z0 + l1 / 2)
        l2 = h * g(x0 + h / 2, y0 + k1 / 2, z0 + l1 / 2)

        k3 = h * f(x0 + h / 2, y0 + k2 / 2, z0 + l2 / 2)
        l3 = h * g(x0 + h / 2, y0 + k2 / 2, z0 + l2 / 2)

        k4 = h * f(x0 + h, y0 + k3, z0 + l3)
        l4 = h * g(x0 + h, y0 + k3, z0 + l3)

        k = (k1 + 2 * k2 + 2 * k3 + k4) / 6

        print("k: ", k)
        l = (l1 + 2 * l2 + 2 * l3 + l4) / 6
        print("l: ", l)

        yn = y0 + k
        zn = z0 + l

        y_values.append(yn)
        z_values.append(zn)

        print("\t", f"{x0:.6f}\t{y0:.6f}\t{z0:.6f}\t{yn:.6f}\t{zn:.6f}")

        y0 = yn
        x0 += h
        z0 += l

        x_values.append(x0)

    return x_values, y_values


print(">>>>>>>>>>>> RK Method of Order 4 for 1st Order Diff-Eq <<<<<<<<<<<<")

# main()
# User inputs
equation_f = input("Enter the f(x,y,z): ")
equation_g = input("Enter the g(x,y,z): ")
x0 = float(input("Enter initial value of x (x0): "))
y0 = float(input("Enter initial value of y (y0): "))
z0 = float(input("Enter initial value of z (z0): "))
xn = float(input("Enter calculation point (xn): "))
step_size = float(input("Enter step size (h): "))

# Call RK4 method
x_value, y_value = rk4(x0, y0, z0, xn, step_size)

# Plotting
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('RK Method of Order 4 for 1st Order Diff-Eq')
plt.grid(True)
plt.show()

# f(x,y,z): z
# g(x,y,z): -4*z -4*y
# initial value of x (x0): 0
# initial value of y (y0): 0
# initial value of z (z0): 1
# calculation point (xn): 0.2
# step size (h): 0.1


# f(x,y,z): z
# g(x,y,z): 1 + x*y - x**2*z
# initial value of x (x0): 0
# initial value of y (y0): 1
# initial value of z (z0): 0
# calculation point (xn): 0.5
# step size (h): 0.1
