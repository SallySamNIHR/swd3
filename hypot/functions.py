def addition(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return "Please enter int or float"
    return a + b


def squared(a):
    return a * a


def square_root(a):
    return a**0.5


def hypot(a, b):
    sqr_a = squared(a)
    sqr_b = squared(b)
    sum_sqr_a_b = sqr_a + sqr_b
    return square_root(sum_sqr_a_b)
