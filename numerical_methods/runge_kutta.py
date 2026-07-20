def runge_kutta(f, t0, y0, h=1, n=100):
    """Fuction to calculation runge kutta"""
    for _ in range(n):
        k1 = f(t0, y0)
        k2 = f(t0 + h/2, y0 + k1 * h/2)
        k3 = f(t0 + h/2, y0 + k2 * h/2)
        k4 = f(t0 + h, y0 + h * k3)
        y = y0 + h/6 * (k1 + 2 * k2 + 2 *k3 + k4)
        y0 = y
        t0 = t0 + h
    return y0
