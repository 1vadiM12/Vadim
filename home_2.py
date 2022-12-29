def print_max(a, b):
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
    return


min_x(3, 2, 1)


def my_func(q):
    if q > 0:
        print(q)
    else:
        print(-q)

    return q


my_func(-8)


def amount(z, x):
    s = z + x
    return s


print(amount(2, 3))


def zero_number(number):
    if number < 0:
        print("minus")
    elif number > 0:
        print("plus")
    else:
        print("zero")


zero_number(-2)
