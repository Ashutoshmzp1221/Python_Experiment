import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x_points = np.array([0, 1, 2, 3])
y_points = np.array([1, 3, 2, 5])
cs = CubicSpline(x_points, y_points)
x = 1.5
y_interpolated = cs(x)

def plot_the_graph():
    print(f"Cubic Spline Interpolated value at x = {x}: {y_interpolated}")
    x_new = np.linspace(0, 3, 100)
    y_spline = cs(x_new)
    plt.plot(x_points, y_points, 'o', label='Data Points')
    plt.plot(x_new, y_spline, label='Cubic Spline Interpolation')
    plt.legend()
    plt.title('Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()