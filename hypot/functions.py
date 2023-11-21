def addition(a, b):
    """This function returns a plus b. It only takes 2 values.

    :param a: first value
    :type a: int or float
    :param b: second value
    :type b: int or float
    :return: sum of the two inputs
    :rtype: int or float
    """
    if isinstance(a, str) or isinstance(b, str):
        return "Please enter int or float"
    return a + b


def squared(a):
    """_summary_

    :param a: _description_
    :type a: _type_
    :return: _description_
    :rtype: _type_
    """
    return a * a


def square_root(a):
    """_summary_

    :param a: _description_
    :type a: _type_
    :return: _description_
    :rtype: _type_
    """
    return a**0.5


def hypot(a, b):
    """_summary_

    :param a: _description_
    :type a: _type_
    :param b: _description_
    :type b: _type_
    :return: _description_
    :rtype: _type_
    """
    sqr_a = squared(a)
    sqr_b = squared(b)
    sum_sqr_a_b = sqr_a + sqr_b
    return square_root(sum_sqr_a_b)
