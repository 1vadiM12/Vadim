def print_max(a, b, ):
    if a > b:
        print(a, "maximum")
    else:
        print(b, "maximum")


print_max(2, 6)



def min_x(c, d, v):
    if c < d and v > c:
        print(c, "minimum")
    elif d < v:
        print(d, "minimum")
    else:
        print(v, "minimum")


min_x(3, 1, 5)


def amount(z, x):
    s = z + x
    return s


print(amount(2, 3))