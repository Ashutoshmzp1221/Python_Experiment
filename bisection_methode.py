def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError('''The function values at the interval 
                         endpoints must have opposite signs.''')
    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            return c  
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    return (a + b) / 2

def quadratic_function(x):
    return x**2 - 4

def main():
    root = bisection_method(quadratic_function, 0, 3)
    print("Bisection Method Root:", root)

