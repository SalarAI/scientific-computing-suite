def simpsonrule(a, b, f, n=100,method="1/3"):
    """
    Fuction to calculation simpson rule
    """
    if method == "1/3":
        res = 0
        h = (b - a) / n
        for i in range(0, n, 2):
            x0 = a + i * h
            xa = x0 +  h
            xb = x0 + 2 * h
            res += (h/3) * (f(x0) + 4 * f(xa) + f(xb))
        return res
    elif method == "3/8":
        res = 0
        h = (b - a) / n
        for i in range(0, n, 3):
            x0 = a + i * h
            xa = x0 + h
            xb = x0 + 2 * h
            xc = x0 + 3 * h
            res += (3*h/8) * (f(x0) + 3 * f(xa) + 3 * f(xb) + f(xc))
        return res
    else:
        raise KeyError("Error Method")
