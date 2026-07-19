def trapezoidal_rule(a, b, f, n=100):
    """
    Function to calculation trapezoidal rule
    """
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(1, n):
        x0 = a + i * h
        res += 2 * f(x0)
    return (h / 2) * res
