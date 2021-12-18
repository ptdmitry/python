from functools import wraps


def type_logger(func):
    @wraps(func)
    def tag_logger(*args):
        return f'{str(*args)}: {type(*args)}'

    return tag_logger


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
print(calc_cube)