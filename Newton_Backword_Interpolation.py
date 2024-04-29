import numpy


def newton_backward_interpolation(x, y, x_new):
    n = len(x)

    # Create a table to store the divided differences
    divided_differences = numpy.zeros((n, n))

    # Fill in the first column of the divided differences table
    divided_differences[:, 0] = y

    # Calculate the remaining divided differences
    for j in range(1, n):
        for i in range(n - j):
            divided_differences[i, j] = (divided_differences[i + 1, j - 1] - divided_differences[i, j - 1]) / (
                    x[i + j] - x[i])

    # Calculate the interpolated value
    y_new = divided_differences[0, 0]
    for j in range(1, n):
        term = divided_differences[0, j]
        for k in range(j):
            term *= (x_new - x[k])
        y_new += term

    return y_new


years = numpy.array([1941, 1951, 1961, 1971, 1981, 1991])
population = numpy.array([12, 15, 20, 27, 39, 51])
estimated_year1 = 1976
estimated_year2 = 1978

interpolated_population2 = newton_backward_interpolation(years, population, estimated_year2)
interpolated_population1 = newton_backward_interpolation(years, population, estimated_year1)

result = interpolated_population2 - interpolated_population1

print(f"Interpolated population at year {estimated_year1} is: {interpolated_population1:.4f}")
print(f"Interpolated population at year {estimated_year2} is: {interpolated_population2:.4f}")

print(f"Interpolated population from year {estimated_year1}  to {estimated_year2} is: {result:.4f}")
