from functools import wraps


def decor(func):
    print('this is decor')

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('this is wrapper')
        return func(*args, **kwargs)
    # чтобы вернуть фукцию, достаточно вернуть её имя без указания параметров
    return wrapper

p = decor(print)(42,56,67,89)
print(type(p))

