def euler_method(f, y0, t, h = 1, n=100):
    """
    Function to calculation Linear Diferential Equantions
    with euler method
    """
    for _ in range(n):
        y = y0 + h * f(t ,y0)
        y0 = y
    return y
