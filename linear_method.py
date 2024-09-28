import numpy as np
import matplotlib.pyplot as plt
def linear_interpolation(x, x_points, y_points):
    if x < x_points[0] or x > x_points[-1]:
        raise ValueError("x is out of bounds of the interpolation range.")
    
    for i in range(len(x_points) - 1):
        if x_points[i] <= x <= x_points[i+1]:
            x0, x1 = x_points[i], x_points[i+1]
            y0, y1 = y_points[i], y_points[i+1]
            if x == x0 or x == x1: 
                print(f"Interpolation point: ({x0}, {y0}) and ({x1}, {y1})")
            return y0 + (x - x0) * (y1 - y0) / (x1 - x0)
    return None

def plot_the_graph():
    x_points = [0, 1, 2, 3, 4]  
    y_points = [0, 2, 4, 6, 8] 
    x_new = np.linspace(x_points[0], x_points[-1], 100) 
    y_interpolated = [linear_interpolation(x, x_points, y_points) for x in x_new]
    plt.plot(x_points, y_points, 'o', label='Data Points')
    plt.plot(x_new, y_interpolated, label='Linear Interpolation')
    plt.legend()
    plt.title('Linear Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
