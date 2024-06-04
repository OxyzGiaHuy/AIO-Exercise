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

# Trac nghiem cau 9
assert round(approx_cos(x=1, n =10), 2) == 0.54
print(round(approx_cos(x=3.14 , n =10) , 2))
# Output: -1.0

# Trac nghiem cau 10
assert round(approx_sin(x=1, n =10), 4) == 0.8415
print(round(approx_sin(x=3.14, n =10) , 4))
# Output: 0.0016

# Trac nghiem cau 11
assert round(approx_sinh(x = 1, n = 10), 2) == 1.18
print(round(approx_sinh(x = 3.14, n = 10), 2))
# Output: 11.53

# Trac nghiem cau 12
assert round(approx_cosh(x = 1, n = 10), 2) == 1.54
print(round(approx_cosh(x = 3.14, n = 10), 2))
# Output: 11.57
