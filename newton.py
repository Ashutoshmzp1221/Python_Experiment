def newton_raphson_method(func, func_derivative, 
                          initial_guess, 
                          tol=1e-6, max_iter=100):
    x = initial_guess
    iteration = 0
    while abs(func(x)) > tol and iteration < max_iter:
        x = x - func(x) / func_derivative(x)
        iteration += 1
    return x

def cubic_function(x):
    return x**3 - 6*x**2 + 11*x - 6  

def cubic_derivative(x):
    return 3*x**2 - 12*x + 11

def main():
    initial_guess = 1.5
    root_newton = newton_raphson_method(cubic_function, 
                                        cubic_derivative, 
                                        initial_guess)
    print("Newton-Raphson Method Root:", root_newton)

