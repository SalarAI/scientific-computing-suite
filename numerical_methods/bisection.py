def bisection(a, b, f, tol=1e-10, n=100):
    """Fuction to calculation bisection"""
    for _ in range(n):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
