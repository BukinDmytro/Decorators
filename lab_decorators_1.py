#1


def my_decorator_func(func):
    def wrapper():
        print(10 + 10)
        func()
    return wrapper


@my_decorator_func
def func1():
    print(10)
func1()
