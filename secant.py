def secant_method(f, x0, x1, tol=1e-7, max_iter=100):
    for _ in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        if abs(fx1) < tol:
            return x1
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        if abs(x2 - x1) < tol:
            return x2
        
        x0, x1 = x1, x2

    return x1

f = lambda x: x**2 - 4*x + 3  
root = secant_method(f, x0=0, x1=2)  
print("-----------------WELCOME---------------------")
print("Ashutosh Dwivedi--------------------21BCS2617\n")
print(f"Root found by Secant Method: {root}")