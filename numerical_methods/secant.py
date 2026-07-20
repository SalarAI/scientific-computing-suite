def secant(f, x0, x1, tol = 1e-10, n = 100):
    """
    Function to finding finding root
    """
    for n in range(n):
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    return x2
