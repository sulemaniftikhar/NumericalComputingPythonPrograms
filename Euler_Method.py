import matplotlib.pyplot as plt

x_values = []
y_values = []


def euler_method(f, x0, y0, h, xn):
    """
    Solves the ODE dy/dx = f(x, y) using the Explicit Euler method.

    Args:
        f: A function that computes the derivative dy/dx.
        x0: Initial value of x.
        y0: Initial value of y.
        h: Step size.
        xn: Calculation point.

    Returns:
        Arrays containing x and y values.
    """

    print("\n----------- Iteration Table -----------")
    print("n\t x(n)\t\ty(n)\t\ty(n+1)")
    print("---------------------------------------")

    x_values.append(x0)
    y_values.append(y0)

    i = 0
    while x_values[-1] < xn:
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * f(x_values[-1], y_values[-1])
        x_values.append(x_new)
        y_values.append(y_new)

        print(i, "\t", f"{x0:.6f}\t{y0:.6f}\t{y_new:.6f}")
        i += 1

        y0 = y_new
        x0 += h

    return x_values, y_values


print(">>>>>>>>>>>> Euler Method <<<<<<<<<<<<")
# main()
# Prompt the user for function input
function_str = input("Enter the function f(x, y): ")
my_function = eval("lambda x, y: " + function_str)  # Convert string to function

# Prompt the user for initial values
x0 = float(input("Enter the initial value of x: "))
y0 = float(input("Enter the initial value of y: "))

# Prompt the user for step size
step_size = float(input("Enter the step size (h): "))
xn = float(input("Enter calculation point (xn): "))

# Compute using Euler Method
x_values, y_values = euler_method(my_function, x0, y0, step_size, xn)

# Print the results with six decimal places
print("\nAt x = {:.6f}, y = {:.6f}".format(x_values[-1], y_values[-1]))

# Ploting the lists X-Values and Y-Values
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler Method')
plt.grid(True)
plt.show()

# function f(x, y): -(2*y)/x + 2/(3*x) - (4*(1)*(x))/3
#  initial value of x: 0.1
# initial value of y: 0.1
# step size (h): 0.7
# calculation point (xn): 5

# function f(x, y): -(x * y**2 + y)
# initial value of x: 0
# initial value of y: 1
# step size (h): 0.1
# calculation point (xn): 1