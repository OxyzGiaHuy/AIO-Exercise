def factorial(n):
    factor = 1
    for i in range(1, n + 1):
        factor *= i
    return factor


def approx_sin(x, n):
    sin = 0
    for i in range(0, n):
        sin += ((-1)**i) * (x**(2*i+1)) / factorial(2*i+1)
    return sin


def approx_cos(x, n):
    cos = 0
    for i in range(0, n):
        cos += ((-1)**i) * (x**(2*i)) / factorial(2*i)
    return cos


def approx_sinh(x, n):
    approx_sinh = 0
    for i in range(0, n):
        approx_sinh += (x**(2*i+1)) / factorial(2*i+1)
    return approx_sinh


def approx_cosh(x, n):
    cosh = 0
    for i in range(0, n):
        cosh += (x**(2*i)) / factorial(2*i)
    return cosh
