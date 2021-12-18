from functools import wraps


def val_checker(_func):
    def _val_checker(func):

        @wraps(func)
        def wrapper(x):
            if _func(x):
                print(func(x))
            else:
                print('ValueError')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

try:
    a = calc_cube(5)
    print(calc_cube)
except (ValueError, TypeError) as err:
    print(err)