def md_nre(y, y_hat, n, p):
    return (y**(1/n) - y_hat**(1/n))**p


print(md_nre(100, 99.5, 2, 1))
print(md_nre(100, 99, 2, 1))
