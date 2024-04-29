import numpy
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Load the data from the file
data = numpy.loadtxt('bps.dat')

# Extract the columns you want to use for interpolation and plotting
x = data[:, 0]  # First column
y = data[:, 1]  # Second column

# Create a cubic spline interpolation object
cubic_spline = CubicSpline(x, y)

# Generate points for interpolation
x_interp = numpy.linspace(x[0], x[-1], 1000)
y_interp = cubic_spline(x_interp)

# Plot the original data and interpolated curve
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_interp, y_interp, label='Interpolated Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()
