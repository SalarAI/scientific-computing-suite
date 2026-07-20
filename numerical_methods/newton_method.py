def newton_raphson(f, df, x0, tol = 1e-10, max_iter=100):
    """Function to calculation newton raphson"""
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)

        if abs(x_new - x) < tol:
            return x_new
        x = x_new
